# Generated by Django 5.0 on 2023-12-14 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_rename_companyname_businessform_company_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='businessform',
            old_name='AuthorisedBy',
            new_name='Authorised_By',
        ),
        migrations.RenameField(
            model_name='businessform',
            old_name='department',
            new_name='Department',
        ),
        migrations.RenameField(
            model_name='businessform',
            old_name='emailAddress',
            new_name='Email_Address',
        ),
        migrations.RenameField(
            model_name='businessform',
            old_name='M_CreditAmount',
            new_name='Job_Title',
        ),
        migrations.RenameField(
            model_name='businessform',
            old_name='jobTitle',
            new_name='Monthly_Credit_Amount',
        ),
        migrations.RenameField(
            model_name='businessform',
            old_name='M_Spend',
            new_name='Monthly_Spend',
        ),
        migrations.RenameField(
            model_name='businessform',
            old_name='natureOfBusiness',
            new_name='Nature_Of_Business',
        ),
        migrations.RenameField(
            model_name='businessform',
            old_name='telePhoneNumber',
            new_name='TelePhone_Number',
        ),
        migrations.RenameField(
            model_name='businessform',
            old_name='temsAndConditions',
            new_name='Terms_And_Conditions',
        ),
        migrations.RenameField(
            model_name='businessform',
            old_name='websiteAddress',
            new_name='Website_Address',
        ),
        migrations.RenameField(
            model_name='businessform',
            old_name='yearCompanyEst',
            new_name='Year_Company_Est',
        ),
    ]