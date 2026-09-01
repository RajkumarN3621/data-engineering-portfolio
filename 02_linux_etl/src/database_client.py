class DatabaseClient:
    """Generic database abstraction for the portfolio example."""

    def __init__(self, source_system: str):
        self.source_system = source_system

    def read_sql(self, query: str):
        if not query.strip():
            raise ValueError("Query cannot be empty")

        # Production implementation would use the approved connector
        # for Teradata, Oracle, SQL Server, or the target warehouse.
        print(f"Reading from {self.source_system}")
        return None

    def execute(self, query: str):
        if not query.strip():
            raise ValueError("Query cannot be empty")

        print(f"Executing SQL on {self.source_system}")

    def close(self):
        print("Database connection closed")
