# Generated by Django 4.2.3 on 2023-07-30 15:01

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={
                            "unique": "A user with that username already exists."
                        },
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name="username",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, verbose_name="email address"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                (
                    "role",
                    models.CharField(
                        choices=[
                            ("ADMIN", "Admin"),
                            ("CUSTOMER", "Customer"),
                            ("ORGANIZER", "Organizer"),
                        ],
                        max_length=50,
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="Cart",
            fields=[
                (
                    "id",
                    models.CharField(max_length=200, primary_key=True, serialize=False),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Event",
            fields=[
                ("eventID", models.AutoField(primary_key=True, serialize=False)),
                ("eventNAME", models.CharField(max_length=200)),
                ("eventDATE", models.DateField()),
                ("eventDISCRIPTION", models.TextField()),
                ("eventLOCATION", models.CharField(max_length=200)),
                ("eventSTARTTIME", models.TimeField()),
                ("eventADDRESS", models.CharField(max_length=200)),
                ("eventIMAGE", models.ImageField(upload_to="uploads/images/")),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TicketPurchase",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("user_id", models.IntegerField()),
                ("event_name", models.CharField(max_length=255)),
                ("package_name", models.CharField(max_length=255)),
                ("package_price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("quantity", models.IntegerField()),
                ("subtotal", models.DecimalField(decimal_places=2, max_digits=10)),
                ("purchase_date", models.DateTimeField(auto_now_add=True)),
                ("stripe_session_id", models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="TicketPackage",
            fields=[
                ("packageID", models.AutoField(primary_key=True, serialize=False)),
                ("package_name", models.CharField(max_length=200)),
                ("package_description", models.TextField()),
                ("package_price", models.DecimalField(decimal_places=2, max_digits=7)),
                ("package_ticketquantity", models.IntegerField()),
                (
                    "eventID",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ticket_packages",
                        to="events.event",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Ticket",
            fields=[
                ("ticketID", models.AutoField(primary_key=True, serialize=False)),
                ("ticket_type", models.CharField(max_length=200)),
                ("ticket_quantity", models.IntegerField()),
                ("ticket_price", models.DecimalField(decimal_places=2, max_digits=7)),
                ("ticket_description", models.TextField()),
                (
                    "packageID",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tickets",
                        to="events.ticketpackage",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="QRCode",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("qr_code_image", models.ImageField(upload_to="qrcodes/")),
                (
                    "ticket_purchase",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="events.ticketpurchase",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="OrganizerProfile",
            fields=[
                ("organizerID", models.AutoField(primary_key=True, serialize=False)),
                ("organizerREGNO", models.CharField(max_length=200)),
                ("organizerPHONE", models.CharField(max_length=20)),
                ("organizerNIC", models.CharField(max_length=20)),
                ("addressLINE1", models.CharField(default="", max_length=200)),
                ("addressLINE2", models.CharField(default="", max_length=200)),
                ("organizerCITY", models.CharField(default="", max_length=200)),
                ("organizerAGREED", models.BooleanField(default=False)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CustomerProfile",
            fields=[
                ("customerID", models.AutoField(primary_key=True, serialize=False)),
                ("customerPHONE", models.CharField(max_length=20)),
                ("customerNIC", models.CharField(max_length=20)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CartItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantity", models.IntegerField()),
                (
                    "cart",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="items",
                        to="events.cart",
                    ),
                ),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="events.event"
                    ),
                ),
                (
                    "ticket_package",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="events.ticketpackage",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Customer",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("events.user",),
            managers=[
                ("customers", django.db.models.manager.Manager()),
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="Organizer",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("events.user",),
            managers=[
                ("organizer", django.db.models.manager.Manager()),
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
