# Djoser авторизация + регистрация

Привет. Сегодня мы рассмотрим авторизацию + регистрацию на django, используя Djoser. Сначала разберём метод со стандартным модулем для токенов внутри DRF.

## Djoser + DRF

[Подробнее тут](https://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication)

Если Djoser не установлен:

```bash
$ pip install djoser
```

Дописываем файлики:

### django_freelance/settigns.py

```python
INSTALLED_APPS = [
    ...
    'rest_framework.authtoken'
]
```

```bash
$ make migrate
```

### freelance/urls.py

```python
...
from rest_framework.authtoken.views import obtain_auth_token
...

urlpatterns = [
	path('auth/', include('djoser.urls')),
	path('auth/token', obtain_auth_token, name='token'),
...
]
```

### freelance/views.py

```python
...
from rest_framework import permissions

...

class Logout(APIView):

    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

...
	# для каждого view, который должен быть защищён
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

...
```

Не забывайте прописывать Token в заголовках запроса:

```bash
$ curl -X GET http://127.0.0.1:8000/api/example/ -H 'Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b'
```

## Djoser + JWT

Устанавливаем модуль:

```bash
$ pip install djangorestframework_simplejwt
```

### django_freelance/settings.py

```python
...
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [ 
        'rest_framework.permissions.IsAuthenticated',
    ],
    "DEFAULT_PARSER_CLASSES": [
        "rest_framework.parsers.JSONParser", 
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework_simplejwt.authentication.JWTAuthentication"
    ]
}
...
```

### freelance/urls.py

```python
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    ...
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    ...
]
```

Проверка:

```bash
$ curl \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{"username": "davidattenborough", "password": "boatymcboatface"}' \
  http://localhost:8000/api/token/

...
{
  "access":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX3BrIjoxLCJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiY29sZF9zdHVmZiI6IuKYgyIsImV4cCI6MTIzNDU2LCJqdGkiOiJmZDJmOWQ1ZTFhN2M0MmU4OTQ5MzVlMzYyYmNhOGJjYSJ9.NHlztMGER7UADHZJlxNG0WSi22a2KaYSfd1S-AuT7lU",
  "refresh":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX3BrIjoxLCJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImNvbGRfc3R1ZmYiOiLimIMiLCJleHAiOjIzNDU2NywianRpIjoiZGUxMmY0ZTY3MDY4NDI3ODg5ZjE1YWMyNzcwZGEwNTEifQ.aEoAYkSJjoWH1boshQAaTkf8G3yn0kapko6HFRt7Rh4"
}
```

### freelance/views.py

```python
from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied


class IsOwner(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


# для любого view, который нужно закрыть
...
    permission_classes = (IsOwner,)

    def get_queryset(self):
        user = self.request.user
        
        if user.is_authenticated:
            return Model.objects.filter(owner=user)
        
        raise PermissionDenied()
```
