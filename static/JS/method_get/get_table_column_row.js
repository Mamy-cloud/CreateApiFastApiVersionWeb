
//------------------------------------------code avec module create thead------------------
// get_table.js
//-----------------------------get column
//si on veut avoir uniquement la colonne, on enlève import { buildTableRows }
//et buildTableRows(tbody, data, columns);
//et aussi le tbody, script dans le html;
//------------------------------get row
//si on veut avoir uniquement la colonne, on enlève import { buildTableHeader }
//et buildTableRows(tbody, data, columns);
//et aussi le thead, script dans le html;


import { buildTableHeader } from "../component_ui/display_table_header.js";
import { buildTableRows } from "../component_ui/display_table_row.js";

const GettableName = window.location.pathname.split("/").pop();

function loadTable() {
  fetch(`/admin/${GettableName}/get_table`)
    .then(response => response.json())
    .then(data => {
      const thead = document.getElementById("columnsTable");
      const tbody = document.getElementById("rowsTable");

      document.getElementById("tableTitle").textContent =
      "Colonnes de la table : " + data.table;

      // Colonnes = data.columns (avec name + type)
      let columns = data.columns;

      // --- Création de l’en-tête ---
      buildTableHeader(thead, columns);

      // --- Création des lignes ---
      buildTableRows(tbody, data, columns);
    })
    .catch(error => {
      console.error("Erreur lors du chargement du tableau:", error);
    });
}



document.addEventListener("DOMContentLoaded", loadTable);

