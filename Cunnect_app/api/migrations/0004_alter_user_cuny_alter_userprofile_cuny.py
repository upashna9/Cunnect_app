# Generated by Django 4.1.7 on 2023-03-02 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_user_alter_userprofile_cuny_delete_post_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='CUNY',
            field=models.CharField(choices=[('Baruch College', 'Baruch College'), ('Borough of Manhattan Community College', 'Borough of Manhattan Community College'), ('Bronx Community College', 'Bronx Community College'), ('Brooklyn College', 'Brooklyn College'), ('College of Staten Island', 'College of Staten Island'), ('Craig Newmark Graduate School of Journalism', 'Craig Newmark Graduate School of Journalism'), ('CUNY Graduate Center', 'CUNY Graduate Center'), ('CUNY School of Professional Studies', 'CUNY School of Professional Studies'), ('Guttman Community College', 'Guttman Community College'), ('Hostos Community College', 'Hostos Community College'), ('Hunter College', 'Hunter College'), ('John Jay College of Criminal Justice', 'John Jay College of Criminal Justice'), ('Kingsborough Community College', 'Kingsborough Community College'), ('LaGuardia Community College', 'LaGuardia Community College'), ('Lehman College', 'Lehman College'), ('Macaulay Honors College', 'Macaulay Honors College'), ('Medgar Evers College', 'Medgar Evers College'), ('New York City College of Technology', 'New York City College of Technology'), ('Queens College', 'Queens College'), ('Queensborough Community College', 'Queensborough Community College'), ('The City College of New York', 'The City College of New York'), ('York College', 'York College')], max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='CUNY',
            field=models.CharField(choices=[('Baruch College', 'Baruch College'), ('Borough of Manhattan Community College', 'Borough of Manhattan Community College'), ('Bronx Community College', 'Bronx Community College'), ('Brooklyn College', 'Brooklyn College'), ('College of Staten Island', 'College of Staten Island'), ('Craig Newmark Graduate School of Journalism', 'Craig Newmark Graduate School of Journalism'), ('CUNY Graduate Center', 'CUNY Graduate Center'), ('CUNY School of Professional Studies', 'CUNY School of Professional Studies'), ('Guttman Community College', 'Guttman Community College'), ('Hostos Community College', 'Hostos Community College'), ('Hunter College', 'Hunter College'), ('John Jay College of Criminal Justice', 'John Jay College of Criminal Justice'), ('Kingsborough Community College', 'Kingsborough Community College'), ('LaGuardia Community College', 'LaGuardia Community College'), ('Lehman College', 'Lehman College'), ('Macaulay Honors College', 'Macaulay Honors College'), ('Medgar Evers College', 'Medgar Evers College'), ('New York City College of Technology', 'New York City College of Technology'), ('Queens College', 'Queens College'), ('Queensborough Community College', 'Queensborough Community College'), ('The City College of New York', 'The City College of New York'), ('York College', 'York College')], max_length=100),
        ),
    ]