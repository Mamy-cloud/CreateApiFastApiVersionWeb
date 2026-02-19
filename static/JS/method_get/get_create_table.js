function addColumn() {
    const div = document.createElement("div");
    div.className = "column";
    div.innerHTML = `
        <input type="text" name="column_name" placeholder="Nom de colonne" required>
        <select name="type_of_column">
            ${Object.values(SQL_TYPES).flat().map(t => `<option value="${t}">${t}</option>`).join("")}
        </select>
    `;
    document.getElementById("columns").appendChild(div);
}

document.getElementById("createTableForm").addEventListener("submit", async function(e) {
    e.preventDefault();

    const tableName = document.getElementById("tableName").value;
    const columns = Array.from(document.querySelectorAll(".column")).map(col => {
        return {
            column_name: col.querySelector("input").value,
            type_of_column: col.querySelector("select").value
        };
    });

    const payload = {
        table_name: tableName,
        columns: columns
    };

    try {
        const response = await fetch("/admin/tables/json", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify(payload)
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const result = await response.json();

        // Succès
        alert("✅ La demande est bien remplie, le JSON a été transféré dans le backend !");
        console.log("Réponse du backend :", result);

        // Affichage du JSON formaté
        alert(JSON.stringify(result, null, 2));

        // Rechargement de la page actuelle
        window.location.reload();


    } catch (error) {
        // Erreur côté front ou réseau
        alert("❌ Il y a eu une erreur sur le front. Veuillez vérifier la console.log !");
        console.error("Erreur lors du transfert du JSON :", error);
    }
});
