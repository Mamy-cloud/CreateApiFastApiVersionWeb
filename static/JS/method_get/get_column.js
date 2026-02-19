// Charger les colonnes via l’API
    /* fetch(`/admin/tables/columns/${tableName}`)
        .then(response => response.json())
        .then(data => {
            const tbody = document.getElementById("columnsTable");
            data.forEach(col => {
                const row = document.createElement("tr");
                row.innerHTML = `<td>${col.column_name}</td><td>${col.type_data}</td>`;
                tbody.appendChild(row);
            });
        })
        .catch(err => console.error("Erreur:", err)); */

// Récupérer le nom de la table depuis l'URL
const ColumntableName = window.location.pathname.split("/").pop();

// Fonction pour charger les colonnes et les afficher sur une seule ligne
function loadColumns() {
    fetch(`/admin/tables/columns/${ColumntableName}`)
        .then(response => response.json())
        .then(data => {
            const thead = document.getElementById("columnsTable");
            thead.innerHTML = ""; // vide le <thead> avant d'ajouter

            // Créer une seule ligne pour toutes les colonnes
            const row = document.createElement("tr");

            data.forEach(col => {
                const th = document.createElement("th");
                th.textContent = `${col.column_name} (value: ${col.type_data})`;
                th.style.border = "2px solid black";   // border nécessite une couleur pour s'afficher
                th.style.padding = "5px";
                row.appendChild(th);
            });

            thead.appendChild(row);
        })
        .catch(err => console.error("Erreur:", err));
}

// Appel de la fonction au chargement de la page
document.addEventListener("DOMContentLoaded", loadColumns);

