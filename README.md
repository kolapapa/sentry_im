## Sentry 插件发送IM消息
> 收到sentry notification之后 触发im的消息发送功能


# Quickstart

## Install
```shell
source /www/sentry/bin/activate

pip install -e git+https://github.com/kolapapa/sentry_im.git#egg=sentry_btalk

supervisorctl restart all
```

## Uninstall
```shell
source /www/sentry/bin/activate

pip uninstall sentry_im

supervisorctl restart all
```