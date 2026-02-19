const SQL_TYPES = {
    "numeric": ["INTEGER", "SMALLINT", "BIGINT", "DECIMAL", "FLOAT"],
    "char": ["CHAR", "VARCHAR", "TEXT"],
    "boolean": ["BOOLEAN"],
    "datetime": ["DATE", "TIME", "DATETIME", "TIMESTAMP"],
    "money": ["MONEY", "DECIMAL"],
    "url": ["URL", "IMAGE_URL", "VIDEO_URL"]
};

const DEFAULT_VALUES = {
    "INTEGER": "DEFAULT 0",
    "SMALLINT": "DEFAULT 0",
    "BIGINT": "DEFAULT 0",
    "DECIMAL": "DEFAULT 0.0",
    "FLOAT": "DEFAULT 0.0",
    "CHAR": "DEFAULT ''",
    "VARCHAR": "DEFAULT ''",
    "TEXT": "DEFAULT ''",
    "BOOLEAN": "DEFAULT FALSE",
    "DATE": "DEFAULT CURRENT_DATE",
    "TIME": "DEFAULT CURRENT_TIME",
    "DATETIME": "DEFAULT CURRENT_TIMESTAMP",
    "TIMESTAMP": "DEFAULT CURRENT_TIMESTAMP",
    "MONEY": "DEFAULT 0",
    "URL": "DEFAULT ''",
    "IMAGE_URL": "DEFAULT ''",
    "VIDEO_URL": "DEFAULT ''"
};


// Remplir le select existant dans le DOM
document.addEventListener("DOMContentLoaded", () => {
    const typeSelect = document.getElementById("typeSelect");
    if (!typeSelect) return; // si l'élément n'existe pas, on sort

    // On parcourt toutes les valeurs de SQL_TYPES et on crée des options
    Object.values(SQL_TYPES).flat().forEach(type => {
        const option = document.createElement("option");
        option.value = type;
        option.textContent = type;
        typeSelect.appendChild(option);
    });
});
