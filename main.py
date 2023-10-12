from schema_manager import SchemaManager


class App:
    """Run App."""

    def __init__(self):
        self.data_file_list = ["data/data_1.json", "data/data_2.json"]
        self.schema_manager = SchemaManager()

    def dump_schema(self):
        for index, data_file in enumerate(self.data_file_list):
            self.schema_manager.dump_schema(
                save_path=f"schema/schema_{index + 1}.json",
                data_file=data_file,
                schema_uri=None
            )

    def run(self):
        """Run script."""
        self.dump_schema()


if __name__ == "__main__":
    app = App()
    app.run()
