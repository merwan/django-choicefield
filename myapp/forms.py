from django import forms

from myapp.models import TopLevelDomain


class DomainForm(forms.Form):
    top_level_domain = forms.ChoiceField(
        required=True,
        widget=forms.Select(attrs={'class': 'form-control input-lg'}),
        choices=[(tld.name, str(tld.name))
                 for tld in TopLevelDomain.objects.all()],
        initial="com"
    )
