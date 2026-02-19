async function fetchTables() {
    try {
        const response = await fetch("/admin/tables/list");
        
        if (!response.ok) {
            const text = await response.text();
            console.error("Server response:", text);
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        // ⚡ Ici, on reçoit ton JSON
        const tables = await response.json();  
        //console.table(tables);
        //console.log("Données reçues du serveur :", tables);
        // tables = [{"table_name":"cv_web"},{"table_name":"nouveau_essai"},{"table_name":"essai_16_février"}]

        const tbody = document.getElementById("tablesList");

        // Vider le tableau avant de le remplir
        tbody.innerHTML = "";

        // tables est ton tableau JSON renvoyé par l'API
        tables.forEach(table => {
            const row = document.createElement("tr");

            // Colonne nom de la table
            const nameCell = document.createElement("td");
            nameCell.textContent = table.table_name;

            // Colonne bouton
            const actionCell = document.createElement("td");
            const button = document.createElement("button");
            button.textContent = "Ouvrir";
            button.addEventListener("click", () => {
                window.location.href = `/admin/${table.table_name}`;
            });

            actionCell.appendChild(button);

            // Ajouter les cellules à la ligne
            row.appendChild(nameCell);
            row.appendChild(actionCell);

            // Ajouter la ligne au tableau
            tbody.appendChild(row);
        });


        console.log("Liste des tables chargée :", tables);

    } catch (error) {
        console.error("Erreur lors du chargement des tables :", error);
    }
}

// Appel dès que le script est chargé
fetchTables();
