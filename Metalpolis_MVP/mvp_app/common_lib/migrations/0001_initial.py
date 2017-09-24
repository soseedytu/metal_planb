# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-15 14:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CCodeCategory',
            fields=[
                ('Id', models.AutoField(db_index=True, primary_key=True, serialize=False, unique=True)),
                ('Name', models.CharField(max_length=45)),
                ('Description', models.CharField(max_length=200)),
                ('CreatedDate', models.DateTimeField(auto_now_add=True)),
                ('CreatedBy', models.CharField(max_length=45)),
                ('ModifiedDate', models.DateTimeField(auto_now_add=True)),
                ('ModifiedBy', models.CharField(max_length=45)),
                ('Status', models.IntegerField()),
                ('Version', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CCodeTable',
            fields=[
                ('Id', models.AutoField(db_index=True, primary_key=True, serialize=False, unique=True)),
                ('Name', models.CharField(max_length=45)),
                ('Description', models.CharField(max_length=45)),
                ('CreatedDate', models.DateTimeField(auto_now_add=True)),
                ('CreatedBy', models.CharField(max_length=45)),
                ('ModifiedDate', models.DateTimeField(auto_now_add=True)),
                ('ModifiedBy', models.CharField(max_length=45)),
                ('Status', models.IntegerField()),
                ('Version', models.DateTimeField(auto_now_add=True, null=True)),
                ('CCodeCategory_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common_lib.CCodeCategory')),
                ('CParentCode_Id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='common_lib.CCodeTable')),
            ],
        ),
        migrations.CreateModel(
            name='CTags',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('TagName', models.CharField(db_index=True, max_length=45)),
                ('CreatedDate', models.DateTimeField(auto_now_add=True)),
                ('CreatedBy', models.CharField(max_length=45)),
                ('ModifiedDate', models.DateTimeField(auto_now_add=True)),
                ('ModifiedBy', models.CharField(max_length=45)),
                ('Status', models.IntegerField()),
                ('Version', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MCompany',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=45)),
                ('Address', models.CharField(max_length=200)),
                ('Domain', models.CharField(max_length=45)),
                ('RegNo', models.CharField(max_length=45)),
                ('Code', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='MDocumentNumber',
            fields=[
                ('Id', models.AutoField(db_index=True, primary_key=True, serialize=False, unique=True)),
                ('Name', models.CharField(max_length=45)),
                ('Prefix', models.CharField(max_length=45)),
                ('Suffix', models.CharField(max_length=45)),
                ('Format', models.CharField(max_length=45)),
                ('RunningNumber', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MDServiceParameter',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('ParameterName', models.CharField(max_length=45, null=True)),
                ('ParameterDefaultValues', models.CharField(max_length=15, null=True)),
                ('Uom', models.CharField(max_length=10, null=True)),
                ('Status', models.IntegerField(null=True)),
                ('Version', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MDSupplierServiceParameter',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('ParameterName', models.CharField(max_length=45, null=True)),
                ('MinValue', models.CharField(max_length=45, null=True)),
                ('MaxValue', models.CharField(max_length=45, null=True)),
                ('Uom', models.CharField(max_length=45, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MDSupplierServices',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('MCompany_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common_lib.MCompany')),
            ],
        ),
        migrations.CreateModel(
            name='MDUserRating',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('UserRating', models.IntegerField()),
                ('Comment', models.CharField(max_length=200)),
                ('MUserRatingCol', models.CharField(max_length=45, null=True)),
                ('CreatedDate', models.DateTimeField(auto_now_add=True)),
                ('CreatedBy', models.CharField(max_length=45)),
                ('Version', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MServices',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('ServiceName', models.CharField(db_index=True, max_length=45, unique=True)),
                ('CreatedDate', models.DateTimeField(auto_now_add=True)),
                ('CreatedBy', models.CharField(max_length=45)),
                ('ModifiedDate', models.DateTimeField(auto_now_add=True)),
                ('ModifiedBy', models.CharField(max_length=45)),
                ('Status', models.IntegerField()),
                ('Version', models.DateTimeField(null=True)),
                ('CommonShapeImage', models.BinaryField()),
                ('CMetalType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common_lib.CCodeTable')),
                ('MParentServices_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common_lib.MServices')),
            ],
        ),
        migrations.CreateModel(
            name='MUser',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('EmailAddress', models.CharField(db_index=True, max_length=55)),
                ('Password', models.CharField(max_length=45)),
                ('Username', models.CharField(max_length=45)),
                ('CreatedDate', models.DateTimeField(auto_now_add=True)),
                ('CreatedBy', models.CharField(default='admin', max_length=45)),
                ('ModifiedDate', models.DateTimeField(auto_now_add=True)),
                ('ModifiedBy', models.CharField(default='admin', max_length=45)),
                ('Status', models.IntegerField(default=1000001)),
                ('RfqCount', models.IntegerField(default=0)),
                ('QuoteCount', models.IntegerField(default=0)),
                ('Version', models.DateTimeField(null=True)),
                ('Title', models.CharField(max_length=5)),
                ('ContactNumber', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='TClarifications',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('ClarificationQuestion', models.CharField(max_length=400, null=True)),
                ('ClarificationAnswer', models.CharField(max_length=400, null=True)),
                ('Version', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TDocument',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Title', models.CharField(max_length=45)),
                ('ShortDescription', models.CharField(max_length=45)),
                ('LongDescription', models.CharField(max_length=500)),
                ('SubmissionDate', models.DateTimeField()),
                ('CreatedDate', models.DateTimeField(auto_now_add=True)),
                ('CreatedBy', models.CharField(max_length=45)),
                ('ModifiedDate', models.DateTimeField(auto_now_add=True)),
                ('ModifiedBy', models.CharField(max_length=45)),
                ('Status', models.IntegerField()),
                ('Version', models.DateTimeField(null=True)),
                ('DocumentNo', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='TDRequiredServices',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('MService_Name', models.CharField(max_length=45)),
                ('CreatedDate', models.DateTimeField(auto_now_add=True)),
                ('CreatedBy', models.CharField(max_length=45)),
                ('ModifiedDate', models.DateTimeField(auto_now_add=True)),
                ('ModifiedBy', models.CharField(max_length=45)),
                ('Status', models.IntegerField()),
                ('Version', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TDRequiredServicesParameters',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('ParameterName', models.CharField(max_length=45, null=True)),
                ('ParameterValue', models.CharField(max_length=45, null=True)),
                ('TDRequiredServicesParametersCol', models.CharField(max_length=45, null=True)),
                ('TDRequiredServices_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common_lib.TDRequiredServices')),
            ],
        ),
        migrations.CreateModel(
            name='TFileAttachments',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('FileName', models.CharField(max_length=150)),
                ('FileBinary', models.BinaryField()),
                ('CreatedDate', models.DateTimeField(auto_now_add=True)),
                ('CreatedBy', models.CharField(max_length=45)),
                ('ModifiedDate', models.DateTimeField(auto_now_add=True)),
                ('ModifiedBy', models.CharField(max_length=45)),
                ('Status', models.IntegerField()),
                ('Version', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TTargetedSuppliers',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='MBuyer',
            fields=[
                ('MUser_Id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='common_lib.MUser')),
                ('RfqCount', models.IntegerField(default=0)),
                ('TotalClosedRfqCount', models.IntegerField(default=0)),
                ('TotalWithdrawRfqCount', models.IntegerField(default=0)),
                ('TotalAwardRfqCount', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='MSupplier',
            fields=[
                ('MUser_Id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='common_lib.MUser')),
                ('MServiceTags', models.CharField(max_length=400)),
                ('TotalSubmittedQuotes', models.IntegerField(default=0)),
                ('TotalQuotesWon', models.IntegerField(default=0)),
                ('TotalQuotesMissed', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='TRequestForQuotation',
            fields=[
                ('Document_Id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='common_lib.TDocument')),
                ('Title', models.CharField(max_length=300)),
                ('FinalClosingDate', models.DateTimeField()),
                ('FirstClosingDate', models.DateTimeField()),
                ('RevisedClosingDate1', models.DateTimeField()),
                ('RevisedClosingDate2', models.DateTimeField()),
                ('TotalSubmittedQuotes', models.IntegerField(default=0)),
                ('RequiredServiceTags', models.CharField(max_length=400)),
                ('IsSelected', models.BooleanField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='TSupplierQuotation',
            fields=[
                ('Document_Id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='Document_ID', serialize=False, to='common_lib.TDocument')),
                ('QuotedFigure', models.DecimalField(decimal_places=2, max_digits=13)),
                ('ValidToDate', models.DateTimeField()),
                ('RevisionNo', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='ttargetedsuppliers',
            name='MUser_Id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common_lib.MUser'),
        ),
        migrations.AddField(
            model_name='ttargetedsuppliers',
            name='TDocument_Id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common_lib.TDocument'),
        ),
        migrations.AddField(
            model_name='tfileattachments',
            name='TDocument_Id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common_lib.TDocument'),
        ),
        migrations.AddField(
            model_name='tdrequiredservices',
            name='TRfq_Id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common_lib.TDocument'),
        ),
        migrations.AddField(
            model_name='tdocument',
            name='CDocumentType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Document_Type', to='common_lib.CCodeTable'),
        ),
        migrations.AddField(
            model_name='tdocument',
            name='CQuotationStatus',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Quotation_Status', to='common_lib.CCodeTable'),
        ),
        migrations.AddField(
            model_name='tdocument',
            name='CRfqStatus',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Request_For_Quotation_Status', to='common_lib.CCodeTable'),
        ),
        migrations.AddField(
            model_name='tdocument',
            name='MUser_Id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common_lib.MUser'),
        ),
        migrations.AddField(
            model_name='tclarifications',
            name='MAskingPerson_Id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common_lib.MUser'),
        ),
        migrations.AddField(
            model_name='tclarifications',
            name='TDocument_Id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common_lib.TDocument'),
        ),
        migrations.AddField(
            model_name='muser',
            name='CUserType',
            field=models.ForeignKey(db_index=False, on_delete=django.db.models.deletion.CASCADE, to='common_lib.CCodeTable'),
        ),
        migrations.AddField(
            model_name='muser',
            name='MCompany_Id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='common_lib.MCompany'),
        ),
        migrations.AddField(
            model_name='mduserrating',
            name='MUser_Id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common_lib.MUser'),
        ),
        migrations.AddField(
            model_name='mdsupplierservices',
            name='MServices_Id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common_lib.MServices'),
        ),
        migrations.AddField(
            model_name='mdsupplierserviceparameter',
            name='MDSupplierServices_Id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common_lib.MDSupplierServices'),
        ),
        migrations.AddField(
            model_name='mdserviceparameter',
            name='MServices_Id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common_lib.MServices'),
        ),
        migrations.AddField(
            model_name='tsupplierquotation',
            name='TRfq_Id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Request_For_Quotation_ID', to='common_lib.TDocument'),
        ),
    ]
