from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Executor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=11)

    def __str__(self):
        return "User: {}, phone: {}".format(self.user, self.phone)


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=11)

    def __str__(self):
        return "User: {}, phone: {}".format(self.user, self.phone)


class Service(models.Model):
    SERVICE_TYPES = [
                ('1', 'Веб разработка'),
                ('2', 'Маркетинг'),
                ('3', 'Копирайтинг'),
                ('4', 'Рерайтиинг'),
                ('5', 'Переводы'),
                ('6', 'Видеомонтаж'),
                ('7', 'Фотография')
            ]

    executor = models.ForeignKey(Executor, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    desc = models.CharField(max_length=1000)
    price = models.IntegerField()
    service_type = models.CharField(choices=SERVICE_TYPES, default='1', max_length=1)

    def __str__(self):
        return '{}, {}, price: {}'.format(self.name, self.get_service_type_display(), self.price)


class Order(models.Model):
    ORDER_TYPES = [
                ('1', 'Веб разработка'),
                ('2', 'Маркетинг'),
                ('3', 'Копирайтинг'),
                ('4', 'Рерайтиинг'),
                ('5', 'Переводы'),
                ('6', 'Видеомонтаж'),
                ('7', 'Фотография')
            ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    desc = models.CharField(max_length=1000)
    price = models.IntegerField()
    order_type = models.CharField(choices=ORDER_TYPES, default='1', max_length=1)

    def __str__(self):
        return '{}, {}, price: {}'.format(self.name, self.get_order_type_display(), self.price)


class Tag(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=30)

    def __str__(self):
        return '{}'.format(self.name)


class Ordering(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    executor = models.ForeignKey(Executor, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)
    order_date = models.DateTimeField()
    deadline = models.DateTimeField()

    def __str__(self):
        return '{} - {}, Customer: {}, Executor: {}'.format(self.order_date, self.deadline, self.customer, self.executor)


class Message(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    executor = models.ForeignKey(Executor, on_delete=models.CASCADE)
    msg_date = models.DateTimeField()
    is_edited = models.BooleanField(default=False)
    desc = models.CharField(max_length=1000)


class Ticket(models.Model):
    SEVERITIES = [
                ('1', 'Низкая'),
                ('2', 'Средняя'),
                ('3', 'Высокая')
            ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True)
    executor = models.ForeignKey(Executor, on_delete=models.CASCADE, blank=True, null=True)
    severity = models.CharField(choices=SEVERITIES, default='1', max_length=1)
    desc = models.CharField(max_length=1000)
    ticket_date = models.DateTimeField()
    is_resolved = models.BooleanField(default=False)

    def __str__(self):
        return '{}, {}, Is resolved? {}'.format(self.get_severity_display(), self.ticket_date, self.is_resolved)


class Review(models.Model):
    RATING_FILLED = [
                ('1', 1),
                ('2', 2),
                ('3', 3),
                ('4', 4),
                ('5', 5)
            ]

    rating = models.CharField(choices=RATING_FILLED, default='1', max_length=1)
    desc = models.CharField(max_length=1000)


class Authoring(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True)
    executor = models.ForeignKey(Executor, on_delete=models.CASCADE, blank=True, null=True)
    review_date = models.DateTimeField()

    def __str__(self):
        return '{}, {}'.format(self.author, self.review_date)

