## Sentry 插件发送btalk消息
> 收到sentry notification之后 触发btalk的消息发送功能


# Quickstart

## Install
```shell
source /www/sentry/bin/activate

pip install -e git+http://git.corp.bianlifeng.com/devops-rd/sentry-btalk.git#egg=sentry_btalk

supervisorctl restart all
```

## Uninstall
```shell
source /www/sentry/bin/activate

pip uninstall sentry_btalk

supervisorctl restart all
```