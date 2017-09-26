from django.db import models
from django.contrib.auth.models import update_last_login, user_logged_in

# Create your models here.


class MDocumentNumber(models.Model):
    Id = models.AutoField(primary_key=True, unique=True, db_index=True)  # system will add automatically
    Name = models.CharField(max_length=45)
    Prefix = models.CharField(max_length=45)
    Suffix = models.CharField(max_length=45)
    Format = models.CharField(max_length=45)
    RunningNumber = models.IntegerField(null=False)

    def __str__(self):
        return self.Id

class CCodeCategory(models.Model):
    Id = models.AutoField(primary_key=True, unique=True, db_index=True)  # system will add automatically
    Name = models.CharField(max_length=45)
    Description = models.CharField(max_length=200)
    CreatedDate = models.DateTimeField(auto_now_add=True, null=False)
    CreatedBy = models.CharField(max_length=45, null=False)
    ModifiedDate = models.DateTimeField(auto_now_add=True, null=False)
    ModifiedBy = models.CharField(max_length=45, null=False)
    Status = models.IntegerField(null=False)
    Version = models.DateTimeField(null=True)

    def __str__(self):
        return self.Name

class CCodeTable(models.Model):
    Id = models.AutoField(primary_key=True, unique=True, db_index=True)  # system will add automatically
    Name = models.CharField(max_length=45, null=False)
    Description = models.CharField(max_length=45, null=False)
    CreatedDate = models.DateTimeField(auto_now_add=True, null=False)
    CreatedBy = models.CharField(max_length=45, null=False)
    ModifiedDate = models.DateTimeField(auto_now_add=True, null=False)
    ModifiedBy = models.CharField(max_length=45, null=False)
    Status = models.IntegerField(null=False)
    CCodeCategory_Id = models.ForeignKey(CCodeCategory, db_index=True)
    CParentCode_Id = models.ForeignKey('self', db_index=True, null=True, blank=True)
    Version = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.Description

class MCompany(models.Model):
    Id = models.AutoField(primary_key=True)  # system will add automatically
    Name = models.CharField(max_length=45, null=False)
    Address = models.CharField(max_length=200, null=False)
    Domain = models.CharField(max_length=45, null=False)
    RegNo = models.CharField(max_length=45, null=False)
    Code = models.CharField(max_length=45, null=False)

    def __str__(self):
        return self.Name

class MUser(models.Model):
    Id = models.AutoField(primary_key=True)
    EmailAddress = models.CharField(max_length=55, null=False, db_index=True)
    Password = models.CharField(max_length=45, null=False)
    Username = models.CharField(max_length=45, null=False)
    CUserType = models.ForeignKey(CCodeTable, db_index=False)
    CreatedDate = models.DateTimeField(auto_now_add=True, null=False)
    CreatedBy = models.CharField(max_length=45, null=False, default="admin")
    ModifiedDate = models.DateTimeField(auto_now_add=True, null=False)
    ModifiedBy = models.CharField(max_length=45, null=False, default="admin")
    Status = models.IntegerField(null=False, default=1000001)
    RfqCount = models.IntegerField(default=0)
    QuoteCount = models.IntegerField(default=0)
    Version = models.DateTimeField(null=True)
    Title = models.CharField(max_length=5)
    ContactNumber = models.CharField(max_length=45)
    MCompany_Id = models.ForeignKey(MCompany, db_index=True, null=True)

    def __str__(self):
        return self.EmailAddress

    def check_password(self, raw_password):
        # TODO: Make this auto update using
        # check_passwords setter argument
        return check_password(raw_password, self.password)

class MBuyer(models.Model):
    MUser_Id = models.OneToOneField(MUser, primary_key=True, db_index=True)
    RfqCount = models.IntegerField(default=0)
    TotalClosedRfqCount = models.IntegerField(default=0)
    TotalWithdrawRfqCount = models.IntegerField(default=0)
    TotalAwardRfqCount = models.IntegerField(default=0)

class MSupplier(models.Model):
    MUser_Id = models.OneToOneField(MUser, primary_key=True, db_index=True)
    MServiceTags = models.CharField(max_length=400)
    TotalSubmittedQuotes = models.IntegerField(default=0)
    TotalQuotesWon = models.IntegerField(default=0)
    TotalQuotesMissed = models.IntegerField(default=0)


class CTags(models.Model):
    Id = models.AutoField(primary_key=True) # system will add automatically
    TagName = models.CharField(max_length=45, db_index=True)
    CreatedDate = models.DateTimeField(auto_now_add=True, null=False)
    CreatedBy = models.CharField(max_length=45, null=False)
    ModifiedDate = models.DateTimeField(auto_now_add=True, null=False)
    ModifiedBy = models.CharField(max_length=45, null=False)
    Status = models.IntegerField(null=False)
    Version = models.DateTimeField(null=True)

    def __str__(self):
        return self.TagName

class MServices(models.Model):
    Id = models.AutoField(primary_key=True) # system will add automatically
    MParentServices_Id = models.ForeignKey('self', db_index=True)
    ServiceName = models.CharField(max_length=45, null=False, unique=True, db_index=True)
    CMetalType = models.ForeignKey(CCodeTable, db_index=True)
    CreatedDate = models.DateTimeField(auto_now_add=True, null=False)
    CreatedBy = models.CharField(max_length=45, null=False)
    ModifiedDate = models.DateTimeField(auto_now_add=True, null=False)
    ModifiedBy = models.CharField(max_length=45, null=False)
    Status = models.IntegerField(null=False)
    Version = models.DateTimeField(null=True)
    CommonShapeImage = models.BinaryField()

    def __str__(self):
        return self.ServiceName

class TDocument(models.Model):
    Id = models.AutoField(primary_key=True)  # system will add automatically
    Title = models.CharField(max_length=45, null=False)
    CDocumentType = models.ForeignKey(CCodeTable, db_index=True, related_name='Document_Type')
    ShortDescription = models.CharField(max_length=45)
    LongDescription = models.CharField(max_length=500)
    SubmissionDate = models.DateTimeField()
    CQuotationStatus = models.ForeignKey(CCodeTable, db_index=True, related_name='Quotation_Status')
    CRfqStatus = models.ForeignKey(CCodeTable, db_index=True, related_name='Request_For_Quotation_Status')
    CreatedDate = models.DateTimeField(auto_now_add=True, null=False)
    CreatedBy = models.CharField(max_length=45, null=False)
    ModifiedDate = models.DateTimeField(auto_now_add=True, null=False)
    ModifiedBy = models.CharField(max_length=45, null=False)
    Status = models.IntegerField(null=False)
    Version = models.DateTimeField(null=True)
    MUser_Id = models.ForeignKey(MUser, db_index=True)
    DocumentNo = models.CharField(max_length=45, null=False)

    def __str__(self):
        return self.Title

class TRequestForQuotation(models.Model):
    Document_Id = models.OneToOneField(TDocument, db_index=True, primary_key=True)
    Title = models.CharField(max_length=300, null=False)
    FinalClosingDate = models.DateTimeField()
    FirstClosingDate = models.DateTimeField()
    RevisedClosingDate1 = models.DateTimeField()
    RevisedClosingDate2 = models.DateTimeField()
    TotalSubmittedQuotes = models.IntegerField(default=0)
    RequiredServiceTags = models.CharField(max_length=400)
    IsSelected = models.BooleanField(default=1)

    def __str__(self):
        return self.Title

class TSupplierQuotation(models.Model):
    Document_Id = models.OneToOneField(TDocument, db_index=True, primary_key=True, related_name='Document_ID')
    TRfq_Id = models.ForeignKey(TDocument, db_index=True, related_name='Request_For_Quotation_ID')
    QuotedFigure = models.DecimalField(max_digits=13, decimal_places=2, null=False)
    ValidToDate = models.DateTimeField()
    RevisionNo = models.IntegerField()


class TDRequiredServices(models.Model):
    Id = models.AutoField(primary_key=True)  # system will add automatically
    MService_Name = models.CharField(max_length=45)
    CreatedDate = models.DateTimeField(auto_now_add=True, null=False)
    CreatedBy = models.CharField(max_length=45, null=False)
    ModifiedDate = models.DateTimeField(auto_now_add=True, null=False)
    ModifiedBy = models.CharField(max_length=45, null=False)
    Status = models.IntegerField(null=False)
    Version = models.DateTimeField(null=True)
    TRfq_Id = models.ForeignKey(TDocument, db_index=True)


class TFileAttachments(models.Model):
    Id = models.AutoField(primary_key=True)  # system will add automatically
    TDocument_Id = models.ForeignKey(TDocument, db_index=True)
    FileName = models.CharField(max_length=150, null=False)
    FileBinary = models.BinaryField(null=False)
    CreatedDate = models.DateTimeField(auto_now_add=True, null=False)
    CreatedBy = models.CharField(max_length=45, null=False)
    ModifiedDate = models.DateTimeField(auto_now_add=True, null=False)
    ModifiedBy = models.CharField(max_length=45, null=False)
    Status = models.IntegerField(null=False)
    Version = models.DateTimeField(null=True)


class MDSupplierServices(models.Model):
    Id = models.AutoField(primary_key=True)  # system will add automatically
    MServices_Id = models.ForeignKey(MServices, db_index=True)
    MCompany_Id = models.ForeignKey(MCompany, db_index=True)


class MDServiceParameter(models.Model):
    Id = models.AutoField(primary_key=True)  # system will add automatically
    ParameterName = models.CharField(max_length=45, null=True)
    ParameterDefaultValues = models.CharField(max_length=15, null=True)
    MServices_Id = models.ForeignKey(MServices, db_index=True)
    Uom = models.CharField(max_length=10, null=True)
    Status = models.IntegerField(null=True)
    Version = models.DateTimeField(null=True)


class TClarifications(models.Model):
    Id = models.AutoField(primary_key=True, null=False)  # system will add automatically
    ClarificationQuestion = models.CharField(max_length=400, null=True)
    ClarificationAnswer = models.CharField(max_length=400, null=True)
    MAskingPerson_Id = models.ForeignKey(MUser, db_index=True)
    TDocument_Id = models.ForeignKey(TDocument, db_index=True)
    Version = models.DateTimeField(null=True)


class MDUserRating(models.Model):
    Id = models.AutoField(primary_key=True)  # system will add automatically
    MUser_Id = models.ForeignKey(MUser, null=False, db_index=True)
    UserRating = models.IntegerField(null=False)
    Comment = models.CharField(max_length=200)
    MUserRatingCol = models.CharField(max_length=45, null=True)
    CreatedDate = models.DateTimeField(auto_now_add=True, null=False)
    CreatedBy = models.CharField(max_length=45, null=False)
    Version = models.DateTimeField(null=True)


class TDRequiredServicesParameters(models.Model):
    Id = models.AutoField(primary_key=True)  # system will add automatically
    TDRequiredServices_Id = models.ForeignKey(TDRequiredServices, null=False, db_index=True)
    ParameterName = models.CharField(max_length=45, null=True)
    ParameterValue = models.CharField(max_length=45, null=True)
    TDRequiredServicesParametersCol = models.CharField(max_length=45, null=True)


class MDSupplierServiceParameter(models.Model):
    Id = models.AutoField(primary_key=True)  # system will add automatically
    MDSupplierServices_Id = models.ForeignKey(MDSupplierServices, db_index=True)
    ParameterName = models.CharField(max_length=45, null=True)
    MinValue = models.CharField(max_length=45, null=True)
    MaxValue = models.CharField(max_length=45, null=True)
    Uom = models.CharField(max_length=45, null=True)


class TTargetedSuppliers(models.Model):
    Id = models.AutoField(primary_key=True)  # system will add automatically
    TDocument_Id = models.ForeignKey(TDocument, db_index=True, null=False)
    MUser_Id = models.ForeignKey(MUser, db_index=True, null=False)

