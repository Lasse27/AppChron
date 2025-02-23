import sqlite3 as sqlite


class DatabaseHandler():
    """
    A class to manage SQLite database connections and execute queries.

    *Attributes*:
        filepath (str): The file path for the SQLite database.
        databaseConnection (sqlite.Connection | None): The active database connection.
    """

    #
    #

    def __init__(self, filepath: str):
        """
        Initialize the DatabaseHandler with the given database file path.

        *Args*:
            filepath (str): The path to the SQLite database file.
        """
        self.filepath: str = filepath
        self.databaseConnection: sqlite.Connection | None = None

    #
    #

    def connect(self) -> None:
        """
        Establish a connection to the SQLite database using extended configuration options.

        *Returns*:
            sqlite.Connection: The active database connection.

        *Raises*:
            sqlite.OperationalError: If the connection fails.
        """
        # Create connection
        self.databaseConnection = sqlite.connect(
            database=self.filepath,
            timeout=10.0,
            detect_types=sqlite.PARSE_DECLTYPES | sqlite.PARSE_COLNAMES,
            isolation_level="IMMEDIATE",
            check_same_thread=False,
            cached_statements=200,
            uri=True
        )

        # PRAGMA for better performance
        self.databaseConnection.execute('PRAGMA journal_mode = WAL')
        self.databaseConnection.execute('PRAGMA synchronous = NORMAL')
        self.databaseConnection.execute('PRAGMA temp_store = MEMORY')

    #
    #

    def runQuery(self, query: str) -> list:
        """
        Execute a given SQL query and return the fetched results.

        *Notes*:
            Make sure that any dynamic parts of the query are properly sanitized or use
            parameterized queries to avoid SQL injection.

        *Args*:
            query (str): The SQL query string to execute.

        *Returns*:
            list: A list of tuples containing the query results.

        *Raises*:
            sqlite.OperationalError: If no connection is established or the query execution fails.
        """

        # Check for existing connection
        if not self.databaseConnection:
            raise sqlite.OperationalError(
                "Database connection is not established. Call connect() first.")

        # Create cursor and execute query on databaseconnection
        cursor = self.databaseConnection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()

        # Close the cursor
        cursor.close()
        return result

    #
    #

    def disconnect(self) -> None:
        """
        Close the active database connection.

        *Returns*:
            None

        *Raises*:
            sqlite.OperationalError: If closing the connection fails.
        """
        self.databaseConnection.close()
