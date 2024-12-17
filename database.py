import sqlite3

DB_NAME = "library.db"

class Database:
  def __enter__(self):
    self.__connection = sqlite3.connect(DB_NAME)
    self.__cursor = self.__connection.cursor()
    return self

  def __exit__(self, type, value, traceback):
    self.__connection.close()

  def execute_wrapper(self, query, params=None, one_row=False):
    if not params:
      results = self.__cursor.execute(query)
    else:
      results = self.__cursor.execute(query, params)

    print("Executed the query and got results", results)

    self.__connection.commit()
    if one_row:
      return results.fetchone()
    else:
      return results.fetchall()