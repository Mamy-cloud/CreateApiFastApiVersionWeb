// previsualisation_component.js
import { addColumn } from "./add_column.js";

// Récupère toutes les colonnes saisies et retourne un JSON validé
export function getColumnsJSON() {
  const rows = document.querySelectorAll("#columnsBody tr.column");
  const columns = [];

  rows.forEach(row => {
    const name = row.querySelector("input[name='column_name']").value.trim();
    const type = row.querySelector("select[name='type_of_column']").value;

    if (name && type) {
      columns.push({ name, type });
    }
  });

  return columns;
}

// Affiche la prévisualisation dans le tableau fourni par ton HTML
export function showPreview(columns) {
  const tbody = document.querySelector("#columnsPreview tbody");
  if (!tbody) return;

  // Réinitialiser le contenu
  while (tbody.firstChild) {
    tbody.removeChild(tbody.firstChild);
  }

  // Ajouter chaque colonne comme une ligne <tr>
  columns.forEach(col => {
    const tr = document.createElement("tr");

    const tdName = document.createElement("td");
    tdName.textContent = col.name;

    const tdType = document.createElement("td");
    tdType.textContent = col.type;

    tr.appendChild(tdName);
    tr.appendChild(tdType);

    tbody.appendChild(tr);
  });
}

// ⚡ Écouteur sur le bouton "Ajouter une colonne"
/* document.getElementById("addColumnBtn").addEventListener("click", () => {
  addColumn(); // ajoute une ligne dans le tableau de saisie
}); */

// ⚡ Écouteur sur le bouton "Prévisualiser"
document.getElementById("previewBtn").addEventListener("click", () => {
  const columns = getColumnsJSON();
  showPreview(columns);
});
