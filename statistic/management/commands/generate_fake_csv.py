import csv
import logging
import os
import re
import random
from typing import List, Type, Optional

from django.db import models, transaction
from django.core.management.base import BaseCommand
from model_utils import Choices

from statistic.models import Student, Faculty, Speciality, Subject, EDUCATION_FORM_CHOICES, GRADE_CHOICES, Mark, \
    SEMESTER_CHOICES

logger = logging.getLogger(__name__)


class GenerateException(Exception):
    pass


HEADERS = ['ФІО', 'СПЕЦІАЛЬНІСТЬ', 'КУРС', 'ФОРМА НАВЧАННЯ', 'ФАКУЛЬТЕТ', 'ПРЕДМЕТ', 'ОЦІНКА', 'СЕМЕСТР']


class Command(BaseCommand):
    help = ''

    def add_arguments(self, parser):
        # Named (optional) arguments
        parser.add_argument(
            '--file',
            type=str,
            nargs='?',
            help='File name',
        )

        parser.add_argument(
            '--count',
            type=int,
            nargs='?',
            help='Count of records',
        )

    def handle(self, *args, **options):
        if options['file'] and options['count']:
            logger.warning(f'File("{options["file"]}") is being generated...')
            self.__generate_csv_file(options['file'], options['count'])
        else:
            logger.error('No file name or count of records!')
