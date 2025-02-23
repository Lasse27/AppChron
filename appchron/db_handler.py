import sqlite3 as sqlite


class DatabaseHandler():
    """
    A class to manage SQLite database connections and execute queries.

    *Attributes*:
        filepath (str): The file path for the SQLite database.
        databaseConnection (sqlite.Connection | None): The active database connection.
    """

    CREATETABLEQUERY: str = """
            CREATE TABLE IF NOT EXISTS "PROCESS_ENTRIES" (
                "auto_id"	    INTEGER NOT NULL UNIQUE,
                "pid"	        INTEGER NOT NULL,
                "name"	        TEXT NOT NULL,
                "durationSec"	INTEGER NOT NULL,
                PRIMARY KEY("auto_id" AUTOINCREMENT)
            );
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
            isolation_level="IMMEDIATE",
            check_same_thread=False,
            cached_statements=200)

    #
    #

    def createTables(self) -> None:
        try:
            # Verbindung zur Datenbank herstellen (wird erstellt, falls sie nicht existiert)
            self.connect()
            print("Datenbank erfolgreich geöffnet/erstellt.")

            # SQL-Befehl zum Erstellen der Tabelle
            self.runQuery(self.CREATETABLEQUERY)

        except Exception as e:
            print(f"Fehler beim Arbeiten mit SQLite: {e}")

        finally:
            self.disconnect()

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
        self.databaseConnection.commit()

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
            sqlite.OperationalError: If closing the connection fails or database connection is not established.
        """
        if not self.databaseConnection:
            raise sqlite.OperationalError(
                "Database connection is not established. Call connect() first.")

        self.databaseConnection.close()


if __name__ == "__main__":
    handler = DatabaseHandler("appchron/data/appchron.sqlite3")
    handler.createTables()
