import datetime
from flask import url_for
from app import db

class BasicSurvey(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    title = db.StringField(max_length=255, required=True)

    # def get_absolute_url(self):
    #     return url_for('post', kwargs={"slug": self.slug})

    def __unicode__(self):
        return self.title

    # meta = {
    #     'allow_inheritance': True,
    #     'indexes': ['-created_at', 'slug'],
    #     'ordering': ['-created_at']
    # }


class BaseController(db.EmbeddedDocument):
    title = db.StringField(max_length=255, required=True)
    type = db.StringField(max_length=255, required=True)

    def __unicode__(self):
        return self.title

    meta = {'allow_inheritance': True}


class RadioButton(BaseController):
    def __init__(self, title):
        super(BaseController, self).__init__()
        self.title = title
        self.type = 'radiobutton'


class CheckBox(BaseController):
    def __init__(self, title):
        super(BaseController, self).__init__()
        self.title = title
        self.type = 'checkbox'


class BaseFormController(db.EmbeddedDocument):
    title = db.StringField(max_length=255, required=True)
    controllers = db.ListField(db.EmbeddedDocumentField('BaseController'))

    def __unicode__(self):
        return self.title

    meta = {'allow_inheritance': True}


class BaseForm(db.Document):
    title = db.StringField(max_length=255, required=True)
    controllers = db.ListField(db.EmbeddedDocumentField('BaseFormController'))

    def __unicode__(self):
        return self.title

    meta = {'allow_inheritance': True}
