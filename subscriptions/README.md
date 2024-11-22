###Integrating into an Existing Project

##Clone the module:

```
git clone https://github.com/your-repo/django-subscription-module.git subscriptions
```

##Configuration steps (Stripe keys).

##Install the Stripe Python SDK:

```
pip install stripe
```

##in -> views.py:

```
import stripe
```

##Add to INSTALLED_APPS:

```
INSTALLED_APPS += ['subscription_module']
```

##Include module URLs:

```
path('subscriptions/', include('subscription_module.urls')),
```

##Run module migrations:

```
python manage.py makemigrations subscription_module
python manage.py migrate
```

##Test integration:

```
python manage.py test subscription_module
```


##Test Stripe with its sandbox environment.