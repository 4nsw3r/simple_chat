# from crispy_forms.bootstrap import FormActions
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Submit, Button
# from django import forms
#
#
# class SubscribeConfirm(forms.Form):
#     def __init__(self, *args, **kwargs):
#         super(SubscribeConfirm, self).__init__(*args, **kwargs)
#
#         self.helper = FormHelper()
#         self.helper.form_class = 'form-horizontal'
#         self.helper.layout = Layout(
#             FormActions(
#                 Submit('addBl', 'Add Block List', css_class='btn-primary'),
#                 Button('cancel', 'Назад', onclick='history.go(-1);'),
#             )
#         )