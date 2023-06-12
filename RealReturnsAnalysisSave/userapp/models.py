# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import AbstractUser


class Roles(models.Model):
    role_name = models.CharField(max_length=25, blank=True, null=True)
    deleted = models.IntegerField()
    for_view = models.IntegerField()
    module_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = "roles"


class Users(models.Model):
    first_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255)
    email_verified_at = models.DateTimeField(blank=True, null=True)
    password = models.CharField(max_length=255)
    remember_token = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    status = models.CharField(max_length=20)
    photo = models.CharField(max_length=60, blank=True, null=True)
    role = models.ForeignKey(Roles, on_delete=models.SET_NULL, blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    referrer_id = models.IntegerField(blank=True, null=True)
    otp = models.IntegerField(blank=True, null=True)
    verify_string = models.CharField(max_length=50, blank=True, null=True)
    transaction_completed = models.IntegerField(blank=True, null=True)
    member_plan = models.IntegerField(blank=True, null=True)
    company_name = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    usage = models.IntegerField(blank=True, null=True)
    stripe_id = models.CharField(max_length=30, blank=True, null=True)
    paypal_id = models.CharField(max_length=30, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = "users"


class Accountchanges(models.Model):
    user_id = models.IntegerField()
    previous_email = models.CharField(max_length=100)
    changed_email = models.CharField(max_length=100)
    verification_link = models.CharField(max_length=100)
    verified = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        db_table = "accountchanges"


class Dscrs(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    borrower_name = models.CharField(max_length=100)
    property_type = models.CharField(max_length=20)
    no_units = models.IntegerField()
    approximate_sq_footage = models.IntegerField()
    property_value = models.IntegerField()
    ltv = models.IntegerField()
    amortization_years = models.IntegerField()
    loan_amount = models.IntegerField()
    interest_rate = models.FloatField()
    down_payment = models.IntegerField()
    down_payment_percentage = models.CharField(max_length=20, blank=True, null=True)
    gross_annual_rental = models.IntegerField()
    other_income = models.IntegerField()
    utilities_telephone = models.IntegerField()
    repairs_maintenance = models.IntegerField()
    salaries_legal = models.IntegerField()
    snow_trash = models.IntegerField()
    re_taxes = models.IntegerField()
    insurance = models.IntegerField()
    other_operating_exp = models.IntegerField()
    annual_operating_exp = models.IntegerField()
    mgmt_fees = models.IntegerField()
    archive = models.IntegerField(blank=True, null=True)
    dscr_ratio = models.CharField(max_length=10, blank=True, null=True)
    report_file = models.CharField(max_length=100, blank=True, null=True)
    cloned = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        db_table = "dscrs"


class Emailcontents(models.Model):
    registration_subject = models.CharField(max_length=100, blank=True, null=True)
    registration_email = models.CharField(max_length=500, blank=True, null=True)
    report_subject = models.CharField(max_length=100, blank=True, null=True)
    report_email = models.CharField(max_length=500, blank=True, null=True)
    account_email_change = models.CharField(max_length=500, blank=True, null=True)
    account_email_change_cubject = models.CharField(
        max_length=100, blank=True, null=True
    )

    class Meta:
        db_table = "emailcontents"


class Escalations(models.Model):
    report_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField()
    subhead = models.CharField(max_length=50)
    repeat_every = models.CharField(max_length=50)
    increment_type = models.IntegerField()
    value_increment = models.CharField(max_length=10)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        db_table = "escalations"


class Faqs(models.Model):
    question = models.CharField(max_length=250, blank=True, null=True)
    deleted = models.IntegerField()
    answer = models.CharField(max_length=250, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = "faqs"


class Heads(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "heads"


class Mails(models.Model):
    driver = models.CharField(max_length=50)
    host = models.CharField(max_length=50)
    port = models.CharField(max_length=50)
    from_address = models.CharField(max_length=50)
    from_name = models.CharField(max_length=50)
    encryption = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=200)

    class Meta:
        db_table = "mails"


class Migrations(models.Model):
    migration = models.CharField(max_length=255)
    batch = models.IntegerField()

    class Meta:
        db_table = "migrations"


class Modules(models.Model):
    module_name = models.CharField(max_length=30)
    module_type = models.IntegerField()
    url_link = models.CharField(max_length=100)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = "modules"


class Notifications(models.Model):
    message = models.CharField(max_length=255, blank=True, null=True)
    related = models.CharField(max_length=25)
    viewed = models.IntegerField()
    record_id = models.IntegerField()
    to_user = models.IntegerField(blank=True, null=True)
    from_user = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = "notifications"


class OauthClients(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    secret = models.CharField(max_length=100, blank=True, null=True)
    redirect = models.CharField(max_length=100, blank=True, null=True)
    personal_access_client = models.CharField(max_length=100, blank=True, null=True)
    password_client = models.CharField(max_length=100, blank=True, null=True)
    revoked = models.CharField(max_length=100, blank=True, null=True)
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        db_table = "oauth_clients"


class OauthPersonalAccessClients(models.Model):
    client_id = models.IntegerField()
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        db_table = "oauth_personal_access_clients"


class PasswordResets(models.Model):
    email = models.CharField(max_length=50)
    token = models.CharField(max_length=100)
    created_at = models.DateTimeField()

    class Meta:
        db_table = "password_resets"


class Permissions(models.Model):
    module = models.ForeignKey(Modules, on_delete=models.CASCADE)
    role = models.ForeignKey(Roles, on_delete=models.CASCADE)
    type = models.CharField(max_length=10, blank=True, null=True)
    permissions = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = "permissions"


class Plans(models.Model):
    plan_name = models.CharField(max_length=25)
    stripe_id = models.CharField(max_length=100, blank=True, null=True)
    paypal_id = models.CharField(max_length=50, blank=True, null=True)
    paypal_no_trial_id = models.CharField(max_length=50, blank=True, null=True)
    price = models.CharField(max_length=5)
    access = models.IntegerField()
    no_reports = models.IntegerField()
    number_of_days = models.IntegerField()
    features = models.CharField(max_length=200)
    upgrade_features = models.CharField(max_length=200)
    deleted = models.IntegerField()
    paypal = models.CharField(max_length=1000)
    cancel = models.CharField(max_length=1000)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = "plans"


class Reports(models.Model):
    user_id = models.IntegerField()
    asset_name = models.CharField(max_length=100)
    acquired_on = models.CharField(max_length=10)
    no_years = models.IntegerField()
    total_sft = models.CharField(max_length=20)
    no_units = models.IntegerField()
    asset_appraisal_type = models.IntegerField()
    asset_appraisal_value = models.IntegerField()
    sales_expense_type = models.IntegerField()
    sales_expense_value = models.IntegerField()
    rent_increase_value = models.IntegerField(blank=True, null=True)
    rent_increases = models.IntegerField(blank=True, null=True)
    original_purchase_price = models.IntegerField()
    amount_down_payment_value = models.IntegerField()
    amount_down_payment = models.IntegerField()
    amount_down_payment_type = models.IntegerField()
    mortgage_loan = models.IntegerField()
    closing_concession = models.IntegerField()
    closing_expenses = models.IntegerField()
    gross_income = models.IntegerField()
    expense_taxes = models.IntegerField()
    taxes_ye_mo = models.IntegerField()
    taxes_frequency = models.IntegerField()
    taxes_increases_type = models.CharField(max_length=30)
    taxes_increase_value = models.CharField(max_length=30)
    taxes_increases_for_every_year = models.CharField(max_length=30)
    expense_hoa = models.IntegerField()
    hoa_ye_mo = models.IntegerField()
    hoa_frequency = models.IntegerField()
    hoa_increases_type = models.CharField(max_length=30)
    hoa_increase_value = models.CharField(max_length=30)
    hoa_increases_for_every_year = models.CharField(max_length=30)
    avg_exp = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    cap_rate = models.FloatField(blank=True, null=True)
    noi = models.IntegerField(blank=True, null=True)
    analysis_type = models.IntegerField()
    expense_vacancy = models.IntegerField(blank=True, null=True)
    expense_vacancy_type = models.IntegerField(blank=True, null=True)
    expense_maintenance = models.IntegerField(blank=True, null=True)
    expense_maintenance_type = models.IntegerField(blank=True, null=True)
    property_mgmt = models.IntegerField(blank=True, null=True)
    property_mgmt_type = models.IntegerField(blank=True, null=True)
    insurance_expense_type = models.IntegerField(blank=True, null=True)
    insurance_expense = models.FloatField()
    insu_ye_mo = models.IntegerField()
    insu_frequency = models.IntegerField()
    insu_increases_type = models.CharField(max_length=30)
    insu_increase_value = models.CharField(max_length=30)
    insu_increases_for_every_year = models.CharField(max_length=30)
    reimbursement_income = models.FloatField(blank=True, null=True)
    reim_ye_mo = models.IntegerField(blank=True, null=True)
    reim_frequency = models.IntegerField(blank=True, null=True)
    reim_increases_type = models.CharField(max_length=30, blank=True, null=True)
    reim_increase_value = models.CharField(max_length=30, blank=True, null=True)
    reim_increases_for_every_year = models.CharField(
        max_length=30, blank=True, null=True
    )
    expense_cam = models.IntegerField(blank=True, null=True)
    cam_frequency = models.IntegerField(blank=True, null=True)
    cam_ye_mo = models.IntegerField(blank=True, null=True)
    cam_increases_type = models.CharField(max_length=30, blank=True, null=True)
    cam_increase_value = models.CharField(max_length=30, blank=True, null=True)
    cam_increases_for_every_year = models.CharField(
        max_length=30, blank=True, null=True
    )
    expense_utilities = models.IntegerField(blank=True, null=True)
    utilities_ye_mo = models.IntegerField(blank=True, null=True)
    utilities_frequency = models.IntegerField(blank=True, null=True)
    utilities_increases_type = models.CharField(max_length=30, blank=True, null=True)
    utilities_increase_value = models.CharField(max_length=30, blank=True, null=True)
    utilities_increases_for_every_year = models.CharField(
        max_length=30, blank=True, null=True
    )
    expense_management = models.IntegerField(blank=True, null=True)
    management_ye_mo = models.IntegerField(blank=True, null=True)
    management_frequency = models.IntegerField(blank=True, null=True)
    management_increases_type = models.CharField(max_length=30, blank=True, null=True)
    management_increase_value = models.CharField(max_length=30, blank=True, null=True)
    management_increases_for_every_year = models.CharField(
        max_length=30, blank=True, null=True
    )
    expense_administrative = models.IntegerField(blank=True, null=True)
    administrative_ye_mo = models.IntegerField(blank=True, null=True)
    administrative_frequency = models.IntegerField(blank=True, null=True)
    administrative_increases_type = models.CharField(
        max_length=30, blank=True, null=True
    )
    administrative_increase_value = models.CharField(
        max_length=30, blank=True, null=True
    )
    administrative_increases_for_every_year = models.CharField(
        max_length=30, blank=True, null=True
    )
    report_file = models.CharField(max_length=100, blank=True, null=True)
    archive = models.IntegerField(blank=True, null=True)
    ammortization_years = models.IntegerField()
    annual_rate_interests = models.CharField(max_length=5)
    debt_service_ratio = models.CharField(max_length=5, blank=True, null=True)
    year1_roi = models.CharField(max_length=50, blank=True, null=True)
    total_roi_percentage = models.CharField(max_length=50, blank=True, null=True)
    total_roi = models.CharField(max_length=50, blank=True, null=True)
    cloned = models.IntegerField()

    class Meta:
        db_table = "reports"


class Settings(models.Model):
    max_bedroom = models.IntegerField()
    max_bathroom = models.IntegerField()
    max_parking = models.IntegerField()
    year_start = models.IntegerField()
    year_end = models.IntegerField()
    basement_status = models.CharField(max_length=500)
    basement_type = models.CharField(max_length=500)
    min_price_range = models.CharField(max_length=500)
    min_rent_range = models.CharField(max_length=500)
    max_price_range = models.CharField(max_length=500)
    max_rent_range = models.CharField(max_length=500)
    loan_approved = models.CharField(max_length=50)
    property_types = models.CharField(max_length=500)
    stages = models.CharField(max_length=500)
    facevalue = models.CharField(max_length=20, blank=True, null=True)
    commission = models.CharField(max_length=20, blank=True, null=True)
    active_report = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = "settings"


class Subheads(models.Model):
    report_id = models.IntegerField()
    user_id = models.IntegerField()
    title = models.CharField(max_length=100)
    amount = models.IntegerField()
    type = models.CharField(max_length=20)
    frequency = models.IntegerField(blank=True, null=True)
    increases_type = models.CharField(max_length=20, blank=True, null=True)
    increase_value = models.CharField(max_length=20, blank=True, null=True)
    increases_for_every_year = models.CharField(max_length=220, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        db_table = "subheads"


class SubscriptionItems(models.Model):
    stripe_id = models.CharField(max_length=40, blank=True, null=True)
    stripe_plan = models.CharField(max_length=40, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    subscription_id = models.IntegerField()
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        db_table = "subscription_items"


class Subscriptions(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    stripe_id = models.CharField(max_length=40, blank=True, null=True)
    stripe_status = models.CharField(max_length=100, blank=True, null=True)
    stripe_plan = models.CharField(max_length=100, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    ends_at = models.DateField(blank=True, null=True)
    expiry = models.DateField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    trial_ends_at = models.DateField(blank=True, null=True)
    amount_paid = models.IntegerField(blank=True, null=True)
    payment_method = models.IntegerField(blank=True, null=True)
    payment_info = models.CharField(max_length=50, blank=True, null=True)
    brand = models.CharField(max_length=20, blank=True, null=True)
    plan_id = models.IntegerField(blank=True, null=True)
    activation = models.CharField(max_length=20)
    trial_allowed = models.CharField(max_length=1, blank=True, null=True)
    access_allowed = models.CharField(max_length=1, blank=True, null=True)
    cron = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = "subscriptions"


class Tenants(models.Model):
    user_id = models.IntegerField()
    tenant_name = models.CharField(max_length=100)
    report_id = models.IntegerField()
    sft_leased = models.CharField(max_length=100)
    lease_rate = models.CharField(max_length=20)
    lease_rate_type = models.IntegerField()
    rent_frequency = models.IntegerField()
    rent_increases = models.CharField(max_length=100)
    rent_increase_value = models.CharField(max_length=100)
    rent_increases_for_every_year = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        db_table = "tenants"


class Wallets(models.Model):
    user_id = models.IntegerField()
    report_id = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    amount = models.IntegerField()
    narration = models.CharField(max_length=100)
    type = models.CharField(max_length=10)
    transaction_id = models.CharField(max_length=50)
    report_type = models.IntegerField(blank=True, null=True)
    refund_date = models.DateField(blank=True, null=True)
    refund_notes = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        db_table = "wallets"
