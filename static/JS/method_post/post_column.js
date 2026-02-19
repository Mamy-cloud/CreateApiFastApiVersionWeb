let columnsToAdd = [];
const addColumntableName = window.location.pathname.split("/").pop();


// Ajouter colonne dans le tableau de prévisualisation
document.getElementById("addColumnBtn").addEventListener("click", () => {
    const name = document.getElementById("columnName").value.trim();
    const type = document.getElementById("typeSelect").value;

    if (!name || !type) {
        alert("Nom et type obligatoires !");
        return;
    }

    columnsToAdd.push({ name, type });

    // Ajouter ligne dans le tableau de prévisualisation
    const row = document.createElement("tr");
    row.innerHTML = `<td>${name}</td><td>${type}</td>`;
    document.getElementById("columnsPreview").appendChild(row);

    // Reset champs
    document.getElementById("columnName").value = "";
    document.getElementById("typeSelect").value = "";
});

// Valider et envoyer les colonnes au backend
document.getElementById("validateColumnsBtn").addEventListener("click", async () => {
    if (columnsToAdd.length === 0) {
        alert("Aucune colonne à ajouter !");
        return;
    }

    try {
        const response = await fetch(`/admin/tables/${addColumntableName}/add-columns`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ columns: columnsToAdd })
        });

        if (!response.ok) throw new Error("Erreur serveur : " + response.status);

        const result = await response.json();
        alert("✅ Colonnes ajoutées avec succès !");
        

        columnsToAdd = [];
        document.getElementById("columnsPreview").innerHTML = "";

        // Rechargement de la page actuelle
        window.location.reload();
    } catch (err) {
        alert("❌ Erreur : " + err.message);
        console.error(err);
    }
});