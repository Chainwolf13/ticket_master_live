from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Ticket(models.Model):
    # class that describes ticket objects user can purchase
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)  # maps ticket information to user
    name = models.CharField(max_length=150, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    address = models.CharField(max_length=150, blank=True, null=True)
    time = models.CharField(max_length=150, blank=True, null=True)
    image = models.CharField(max_length=150, blank=True, null=True)

    # To explain models.ForeignKey     Jah:12/6/23
    #
    # Inside Ticketmaster_ticket table we now have a field called user_id
    # so every ticket can have a user id
    # this is useful because if user is authenticated and we create a ticket
    # then

    def __str__(self):
        return self.name + '---' + self.address  # this.name returns name of this instance

# class UsersCart(models.Model):
#     # one ticket can be on many wishlist
#     # and one wishlist can be ma
#     ticket = models.ManyToManyField(Ticket)
#     # user can wishlist multiple tickets
#     # every ticket can be wishlist by multiple users
#     # ie : Jah -> 15 tickets and
#     # ticket#1 <- jah's wishlist , <- ollie's wishlist ,
