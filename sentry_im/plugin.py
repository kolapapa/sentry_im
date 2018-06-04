# coding: utf-8

import logging
import requests
from sentry.models.useremail import UserEmail
from sentry.plugins.bases import notify
from sentry.utils.cache import cache


IM_API = 'https://im-api/{}/im'


class IMPlugin(notify.NotificationPlugin):
    author = 'kolapapa'
    version = '0.1.0'
    description = 'send trace event to im'

    slug = 'im'
    title = 'im'
    conf_key = 'mail'  # 使用和MailPlugin相同的发送列表
    project_conf_form = None
    project_default_enabled = True

    logger = logging.getLogger('sentry.plugins.im')

    def is_configured(self, project, **kwargs):
        # Nothing configure here
        return True

    def get_send_to(self, project=None):
        if project:
            project_id = project.pk
        else:
            project = ''

        if not (project and project.team):
            return []

        conf_key = self.get_conf_key()
        cache_key = '{}:send_to:{}'.format(conf_key, project_id)

        send_to_list = cache.get(cache_key)
        if send_to_list is None:
            send_to_list = self.get_sendable_users(project)

            send_to_list = filter(bool, send_to_list)
            cache.set(cache_key, send_to_list, 60)

        return send_to_list

    def notify(self, notification):
        event = notification.event
        group = event.group
        project = group.project
        receiver_ids = self.get_send_to(project)
        if not receiver_ids:
            return
        else:
            receivers = []
            for _id in receiver_ids:
                btalk_id = \
                    str(UserEmail.objects.get(id=_id).email).split('@')[0]
                receivers.append(btalk_id)
        link = group.get_absolute_url()
        text = "Sentry project {} notification:\n{}.\nOpen {} to see.".format(
                    project.name, event.message, link)

        send_msg(receivers, text)


def send_msg(receivers=[], message=''):
    if not receivers or not message:
        return
    datas = {
        'message': message
    }
    user_ids = ','.join(receivers)
    r = requests.post(IM_API.format(user_ids), json=datas)
    return (r.status_code, r.text)
