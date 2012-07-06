django-featured-objects
=======================

Django app for making any object featured 

## Requirements

* Django>=1.3

### Installing requirements

    pip install -r requirements.txt

## Testing

    python setup.py

## Configuration

    INSTALLED_APPS += ('featured',)
    FEATURABLE_MODELS = (
        ('app_label', 'model_name'), 
        ('app_label', 'another_model_name')
    )
