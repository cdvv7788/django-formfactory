from django import forms
from django.test import TestCase

from formfactory import models
from formfactory.tests.test_base import load_fixtures


class ModelTestCase(TestCase):
    def setUp(self):
        load_fixtures(self)

    def test_field_constant(self):
        self.assertIn(("DateTimeField", "DateTimeField"), models.FIELD_TYPES)
        self.assertIn(("BooleanField", "BooleanField"), models.FIELD_TYPES)
        self.assertIn(("CharField", "CharField"), models.FIELD_TYPES)

        self.assertIn(("TextInput", "TextInput"), models.WIDGET_TYPES)
        self.assertIn(("DateTimeInput", "DateTimeInput"), models.WIDGET_TYPES)
        self.assertIn(("CheckboxInput", "CheckboxInput"), models.WIDGET_TYPES)

        self.assertIn(
            self.action_data["action"], [a[0] for a in models.FORM_ACTIONS]
        )

        self.assertIn(
            self.dummy_validator,
            [v[0] for v in models.ADDITIONAL_VALIDATORS]
        )

    def test_form(self):
        for key, value in self.form_data.items():
            self.assertEqual(getattr(self.form, key), value)
        self.assertEqual(self.form.fields.count(), len(models.FIELD_TYPES))
        self.assertIsInstance(self.form.as_form(), forms.Form)
        self.assertEqual(
            self.form.get_absolute_url(), "/formfactory/%s/" % self.form.slug
        )

    def test_fieldchoice(self):
        for key, value in self.fieldchoice_data.items():
            self.assertEqual(getattr(self.fieldchoice, key), value)

    def test_formfield(self):
        for count in range(len(models.FIELD_TYPES)):
            formfield_data = getattr(self, "formfield_data_%s" % count)
            for key, value in formfield_data.items():
                formfield = getattr(self, "formfield_%s" % count)
                self.assertEqual(getattr(formfield, key), value)

    def test_formdata(self):
        for key, value in self.formdata_data.items():
            self.assertEqual(getattr(self.formdata, key), value)

    def test_formdataitem(self):
        for key, value in self.formdataitem_data.items():
            self.assertEqual(getattr(self.formdataitem, key), value)