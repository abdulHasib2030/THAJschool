
from django import forms
from accounts.models import Student
from students.models import studentProfile,CourseHistory
from students.content import EDUCATION_LEVEL

# class StudentProfileForm(forms.ModelForm):
    # class Meta:
    #     model = studentProfile
    #     fields = ['student_img', 'first_name', 'last_name', 'email']
        
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for field in self.fields:
    #         self.fields[field].widget.attrs.update({
    #             'class': (
    #                 'appearance-none block w-full bg-gray-200 '
    #                 'text-gray-700 border border-gray-200 rounded '
    #                 'py-3 px-4 leading-tight focus:outline-none '
    #                 'focus:bg-white focus:border-gray-500'
    #             )
    #         })
    #     # jodi user er account thake 
        

    # def save(self, commit=True):
    #     user = super().save(commit=False)
    #     if commit:
    #         user.save()
    #     return user
    

        

########## Update Student Account ##############
# class studentUpdateProfileForm(forms.ModelForm):
    
    # class Meta:
    #     model = Student
    #     fields = ['first_name', 'last_name', 'email']
        

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for field in self.fields:
    #         self.fields[field].widget.attrs.update({
    #             'class': (
    #                 'appearance-none block w-full bg-gray-200 '
    #                 'text-gray-700 border border-gray-200 rounded '
    #                 'py-3 px-4 leading-tight focus:outline-none '
    #                 'focus:bg-white focus:border-gray-500'
    #             )
    #         })
    #     # jodi user er account thake 
        

    # def save(self, commit=True):
    #     user = super().save(commit=False)
    #     if commit:
    #         user.save()

    #     return user
    

class studentUpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['image', 'first_name', 'last_name', 'email']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field in self.fields:
          self.fields[field].widget.attrs.update({
            'class':'form-control'
            })
          
class studentAddressForm(forms.ModelForm):  
    street_address = forms.CharField(max_length=100)
    city = forms.CharField(max_length= 100)
    country = forms.CharField(max_length=100)
    class Meta:
        model = Student
        fields = ['street_address', 'city', 'country']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field in self.fields:
          self.fields[field].widget.attrs.update({
            'class':'form-control'
            })
        # jodi user er account thake 
        if self.instance:
            try:
                user_account = self.instance.student_account              
            except studentProfile.DoesNotExist:
                user_account = None
               
            if user_account:                
                self.fields['street_address'].initial = user_account.street_address
                self.fields['city'].initial = user_account.city   
                self.fields['country'].initial = user_account.country

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()

            user_account, created = studentProfile.objects.get_or_create(user=user) # jodi account thake taile seta jabe user_account ar jodi account na thake taile create hobe ar seta created er moddhe jabe
            user_account.street_address = self.cleaned_data['street_address']
            user_account.city = self.cleaned_data['city']         
            user_account.country = self.cleaned_data['country']
            user_account.save()

        return user
    
class studentEducateionForm(forms.ModelForm):  
    education_level = forms.ChoiceField(choices=EDUCATION_LEVEL)
    institute = forms.CharField(max_length=200)
    passing_year = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    class Meta:
        model = Student
        fields = ['education_level', 'institute', 'passing_year']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field in self.fields:
          self.fields[field].widget.attrs.update({
            'class':'form-control'
            })
        # jodi user er account thake 
        if self.instance:
            try:
                user_account = self.instance.student_account
              
            except studentProfile.DoesNotExist:
                user_account = None
               

            if user_account:
                
                self.fields['institute'].initial = user_account.institute
                self.fields['education_level'].initial = user_account.education_level   
                self.fields['passing_year'].initial = user_account.passing_year

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()

            user_account, created = studentProfile.objects.get_or_create(user=user) # jodi account thake taile seta jabe user_account ar jodi account na thake taile create hobe ar seta created er moddhe jabe

            user_account.education_level = self.cleaned_data['education_level']
            user_account.institute = self.cleaned_data['institute']
          
            user_account.passing_year = self.cleaned_data['passing_year']
            user_account.save()

        return user
    

class studentCourseHistoryForm(forms.ModelForm):
    class Meta:
        model = CourseHistory
        fields = ['course_title', 'payment_method', 'payment_status']
        


