SQL_TYPES = {
    "numeric": ["INTEGER", "SMALLINT", "BIGINT", "DECIMAL", "FLOAT"],
    "char": ["CHAR", "VARCHAR", "TEXT"],
    "boolean": ["BOOLEAN"],
    "datetime": ["DATE", "TIME", "DATETIME", "TIMESTAMP"],
    "money": ["MONEY", "DECIMAL"],
    "url": ["URL", "IMAGE_URL", "VIDEO_URL"]
}

DEFAULT_VALUES = {
    "INTEGER":  0,
    "SMALLINT":  0,
    "BIGINT":  0,
    "DECIMAL": 0.0,
    "FLOAT":  0.0,
    "CHAR":  '',
    "VARCHAR":  '',
    "TEXT":  '',
    "BOOLEAN": "FALSE",
    "DATE": "CURRENT_DATE",
    "TIME": "CURRENT_TIME",
    "DATETIME": "CURRENT_TIMESTAMP",
    "TIMESTAMP": "CURRENT_TIMESTAMP",
    "MONEY": 0,
    "URL": '',
    "IMAGE_URL": '',
    "VIDEO_URL": ''
}
