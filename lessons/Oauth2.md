# Oauth2

## Приложение ВК для авторизации

Сначачала давайте создадим приложение для авторизации. Переходим [сюда](https://vk.com/apps?act=manage), жмём создать приложение, выбираем тип Сайт и вводим туда ссылку (в данном случае, можно 127.0.0.1:8000).

## Пишем бэкенд

Для начала надо установить зависимости:

```bash
pip install django-rest-framework-social-oauth2
```

Теперь добавляем необходимые конфигурационные данные в settings.py:

В секцию INSTALLED_APPS:

```python
INSTALLED_APPS = [
	...
	'oauth2_provider',
	'social_django',
	'rest_framework_social_oauth2'
	...
]
```

Делаем кастомные параметры для хранения данных приложения в соц. сети, через которое будет происходить авторизация:

```python
SOCIAL_AUTH_VK_OAUTH2_KEY = 'id приложения'
SOCIAL_AUTH_VK_OAUTH2_SECRET = 'секретный ключ'
```

В секцию AUTHENTICATION_BACKENDS (если она отсутствует, то добавьте):

```python
AUTHENTICATION_BACKENDS = [
	...
	'social_core.backends.vk.VKOAuth2',
	'rest_framework_social_oauth2.backends.DjangoOAuth2',
	'django.contrib.auth.backends.ModelBackend',
	...
]
```

В секцию настроек REST_FRAMEWORK:

```python
REST_FRAMEWORK = {
	...
	'DEFAULT_AUTHENTICATION_CLASSES': [
		...
		'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
		'rest_framework_social_oauth2.authentication.SocialAuthentication',
		...
	]
}
```

Выполняем миграции:

```bash
cd django-freelance/django_freelance && make migrate
```

Запускаем сервер и переходим в админку:

```bash
make run
```

Создаём новое приложение в админке, выбираем для него суперпользователя. Client type выбираем public. Authorization grant type ставим Client credentials. Даём имя приложению (например, vk_auth), сохраняем.

В urls добавляем:

```python
...
urlpatterns = [
	...
	path('auth/', include('rest_framework_social_oauth2.urls')),
	...
]
...
```

Теперь давайте получим access_token, для этого открываем ссылку: `https://login.vk.com/?act=openapi&oauth=1&aid=<ID вашего приложения>&location=127.0.0.1&new=1&response_type=code`

Копируем полученный access_token и переходим к авторизации.

Открываем постман. Выбираем метод POST, вводим url: `http://127.0.0.1:8000/api/auth/convert-token`.

В form-data прописываем:

grant_type: convert_token
client_id: id приложения для авторизации из django
backend: vk-oauth2
token: access_token из вк

Отпавляем, получаем в ответ jwt-токен, который можем использовать для авторизации и получения данных внутри самого django.

## Список поддерживаемых сервисов для авторизации

Можно найти [здесь](https://python-social-auth.readthedocs.io/en/latest/backends/).
