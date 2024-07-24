from django.db import models


# Create your models here.
class State(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class City(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.state and self.name

    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"


class ChannelMaster(models.Model):
    channel = models.CharField(max_length=150)

    def __str__(self):
        return self.channel

    class Meta:
        verbose_name = "Channel Master"
        verbose_name_plural = "Channel Masters"


class DesignationMaster(models.Model):
    designation = models.CharField(max_length=150)

    def __str__(self):
        return self.designation

    class Meta:
        verbose_name = "Designation Master"
        verbose_name_plural = "Designation Masters"


class ProfessionMaster(models.Model):
    profession = models.CharField(max_length=150)

    def __str__(self):
        return self.profession

    class Meta:
        verbose_name = "Profession Master"
        verbose_name_plural = "Profession Masters"


class ExecutiveMaster(models.Model):
    employee_code = models.CharField(max_length=100)
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.employee_code and self.name

    class Meta:
        verbose_name = "Executive Master"
        verbose_name_plural = "Executive Masters"


class NewMemberEntry(models.Model):
    i_card_number = models.CharField(max_length=100)
    name = models.CharField(max_length=150)
    designation = models.ForeignKey(DesignationMaster, on_delete=models.CASCADE)
    paper_meg_channel = models.CharField(max_length=150)
    valid_upto = models.DateField(auto_now=True)
    executive_name = models.ForeignKey(
        ExecutiveMaster, on_delete=models.CASCADE, related_name="executive_name"
    )
    father_name = models.CharField(max_length=150)
    phone_no = models.CharField(max_length=13)
    mobile_no = models.CharField(max_length=13)
    email = models.EmailField(max_length=254)
    residence = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    pin = models.IntegerField()
    date_of_birth = models.DateField(null=True, blank=True)
    qualification = models.CharField(max_length=50)
    profession = models.ForeignKey(ProfessionMaster, on_delete=models.CASCADE)
    introducer_name = models.ForeignKey(
        ExecutiveMaster, on_delete=models.CASCADE, related_name="introducer_name"
    )
    remark = models.TextField()
    nature_choices = {
        ("Excellent", "Excellent"),
        ("Good", "Good"),
        ("Medium", "Medium"),
        ("Poor", "Poor"),
        ("Very Bad", "Very Bad"),
    }
    nature = models.CharField(max_length=15, choices=nature_choices)

    def __str__(self):
        return self.i_card_number and self.name

    class Meta:
        verbose_name = "Member Entry"
        verbose_name_plural = "Member Entries"
