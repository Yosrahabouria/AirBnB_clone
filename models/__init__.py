#!/usr/bin/python3
"""creation of unique initialization of instance of file storage"""
from models.engine.file_storage import FileStorage

"""instance of fileStorage with Storage"""
Storage = FileStorage()
Storage.reload()
