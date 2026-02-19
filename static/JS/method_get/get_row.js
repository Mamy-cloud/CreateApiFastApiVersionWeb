function loadRows(tableName) {
    fetch(`/admin/tables/rows/${tableName}`)
        .then(response => response.json())
        .then(data => {
            const tbody = document.getElementById("rowsTable");
            tbody.innerHTML = "";
            data.forEach(row => {
                const tr = document.createElement("tr");
                tr.innerHTML = `<td>${row.row_name}</td><td>${row.value_data !== null ? row.value_data : "NULL"}</td>`;
                tbody.appendChild(tr);
            });
        })
        .catch(err => console.error("Erreur:", err));
}

// ⚡ Appel automatique quand la page est prête
document.addEventListener("DOMContentLoaded", () => {
    const pathParts = window.location.pathname.split("/");
    const tableName = pathParts[pathParts.length - 1];
    loadRows(tableName);
});
