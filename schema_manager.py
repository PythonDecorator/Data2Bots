"""
Schema Manager
"""
import os
import json
from genson import SchemaBuilder

basedir = os.path.abspath(os.path.dirname(__file__))


class SchemaManager:
    """Manage schema."""

    def __init__(self):
        self.data = None

    def get_data(self, data_file):
        """Get data"""
        with open(os.path.join(basedir, data_file)) as json_file:
            self.data = json.load(json_file)
            return self.data

    def schema_builder(self, data_file, schema_uri):
        """Build schema from json file and return the schema."""
        builder = SchemaBuilder(schema_uri=schema_uri)
        datastore = self.get_data(os.path.join(basedir, data_file))
        builder.add_object(datastore)

        schema = builder.to_schema()

        return schema

    def dump_schema(self, save_path, data_file, schema_uri):
        """Dump data to a path or folder."""
        with open(os.path.join(basedir, save_path), "w") as json_file:
            json.dump(self.schema_builder(data_file, schema_uri),
                      json_file, indent=2)
