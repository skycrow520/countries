"""SQL Scripts"""

ADD_RECORD = """INSERT INTO {table_name} {fields}
                       VALUES
                       {values};"""

SELECT = """SELECT * from {table_name} WHERE BINARY {qurey_key}={query_val};"""
