from django.conf import settings
from django.core.management import call_command

def main():
    settings.configure(
        INSTALLED_APPS=(
            'django.contrib.contenttypes',
            'django.contrib.auth',
            'featured',
        ),
        DATABASE_ENGINE='sqlite3',
        ROOT_URLCONF = 'tests_urls',
    )
    
    # Fire off the tests
    call_command('test', 'featured')

if __name__ == '__main__':
    main()
