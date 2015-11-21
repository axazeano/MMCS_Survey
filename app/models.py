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