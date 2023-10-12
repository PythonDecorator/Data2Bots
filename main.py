from schema_manager import SchemaManager

data_file_list = ["data/data_1.json", "data/data_2.json"]
schema_manager = SchemaManager()

for index, data_file in enumerate(data_file_list):
    schema_manager.dump_schema(save_path=f"schema/schema_data_{index + 1}.json",
                               data_file=data_file,
                               schema_uri=None)
