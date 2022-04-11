from django import forms
from .models import Topic,Map

class TopicForm(forms.ModelForm):

    class Meta:
        model   = Topic
        fields  = [ "comment" ]


class MapForm(forms.ModelForm):

    class Meta:
        model   = Map
        fields  = [ "data" ]


