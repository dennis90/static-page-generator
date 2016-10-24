import os
import sys

from django.conf import settings

BASEDIR = os.path.dirname(__file__) 

settings.configure(
    DEBUG=True,
    SECRET_KEY='sa35j$Y8&AS98d7f6g670F9*SD&%$)&F%#DS#%A!@F#dfG$fGa%sdf*jDk(k)_/*-+',
    ROOT_URLCONF='sitebuilder.urls',
    MIDDLEWARE_CLASSES=(),
    INSTALLED_APPS=(
        'django.contrib.staticfiles',
        'django.contrib.webdesign',
        'sitebuilder',
    ),
    STATIC_URL='/static/',
    SITE_PAGES_DIRECTORY=os.path.join(BASEDIR, 'pages'),
    SITE_OUTPUT_DIRECTORY=os.path.join(BASEDIR, '_build'),
    STATIC_ROOT=os.path.join(BASEDIR, '_build', 'static'),
)

if __name__ == '__main__':
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)

