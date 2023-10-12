"""
Test for Schema
"""
import os
import unittest
from schema_manager import SchemaManager

basedir = os.path.abspath(os.path.dirname(__file__))


class TestDataSchema(unittest.TestCase):
    """Tests for Data and Schema."""

    def setUp(self) -> None:
        self.schema = SchemaManager()

    def test_data_loads(self):
        """Test read data from the project data directory."""
        res = self.schema.get_data("data/data_1.json")

        self.assertTrue(res)

    def test_building_schema(self):
        """Test That creating schema was successful."""
        test_schema = {'type': 'object', 'properties':
                       {'name': {'type': 'string'},
                        'price': {'type': 'string'}},
                       'required': ['name', 'price']}
        data_file = "data/test.json"
        schema = self.schema.schema_builder(data_file, schema_uri=None)

        self.assertEqual(schema, test_schema)

    def test_dumping_schema(self):
        """Test That dumping schema was successful."""
        dir_ = os.path.join(basedir, "schema/test")
        initial_num_items = len([name for name in os.listdir(dir_)
                                 if os.path.isfile(os.path.join(dir_, name))])

        data_file = "data/test.json"

        save_path = "schema/test/test_schema.json"
        self.schema.dump_schema(save_path=save_path, data_file=data_file, schema_uri=None)

        final_num_items = len([name for name in os.listdir(dir_)
                               if os.path.isfile(os.path.join(dir_, name))])
        self.assertGreater(final_num_items, initial_num_items)

        # remove created test schema
        os.remove(save_path)

    def check_tag_description_exist(self):
        data = self.schema.get_data("schema/example.json")
        if isinstance(data, dict):
            for key, value in data.items():
                res1 = value["tag"]
                res1 = value["description"]
        return self.check_tag_description_exist

    def test_padding_with_tags_and_description(self):
        """Test Padding: Test All attributes in the JSON schema
        are padded with "tag" and "description" keys."""
        data = self.schema.get_data("schema/example.json")
        if isinstance(data, dict):
            for key, value in data.items():
                res1 = value["tag"]
                res2 = value["description"]

                self.assertIsNotNone(res1)
                self.assertIsNotNone(res1)

    def to_get_attributes_from_schema(self):
        data = self.schema.get_data("data/data_1.json")["message"]
        res = data["attributes"]
        return self.to_get_attributes_from_schema

    def test_capturing_only_message_attrs(self):
        """Test schema output captures ONLY the attributes within the
        "message" key of the input JSON source data and all
        attributes within the key "attributes" are excluded."""
        self.assertRaises(KeyError, self.to_get_attributes_from_schema)

    def test_required_set_to_false(self):
        """Test all JSON schema properties "required": false."""
        data = self.schema.get_data("schema/example.json")
        if isinstance(data, dict):
            for key, value in data.items():
                res = data[key]["required"]

                self.assertFalse(res)


if __name__ == '__main__':
    unittest.main()
