# coding=utf-8
from feti.models.course import Course
from haystack import indexes

__author__ = 'Rizky Maulana Nugraha "lucernae" <lana.pcfre@gmail.com>'
__date__ = '24/04/15'


class CourseIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    course_description = indexes.NgramField(
        model_attr='course_description',
        null=True
    )
    course_description_auto = indexes.EdgeNgramField(
        model_attr='course_description',
        null=True
    )
    national_learners_records_database = indexes.CharField(
        model_attr='national_learners_records_database', null=True)

    class Meta:
        app_label = 'feti'

    def get_model(self):
        return Course

    def index_queryset(self, using=None):
        """Used to reindex model"""
        return self.get_model().objects.all()
