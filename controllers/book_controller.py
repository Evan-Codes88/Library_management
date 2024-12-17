from flask import Blueprint, request
from sqlalchemy.exc import IntegrityError
from psycopg2 import errorcodes
from marshmallow import ValidationError

from init import db
from models.book import book_schema, books_schema
from utils.error_handlers import handle_integrity_error, handle_validation_error
from utils.strip import validate_and_strip_field

books_bp = Blueprint("books", __name__, url_prefix = "/books")

