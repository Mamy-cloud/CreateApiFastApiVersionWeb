// tableHeader.js
export function buildTableHeader(thead, columns) {
  thead.innerHTML = ""; // nettoie avant

  const headerRow = document.createElement("tr");
  for (let i = 0; i < columns.length; i++) {
    const th = document.createElement("th");
    th.textContent = columns[i].name + " (" + columns[i].type + ")";
    th.dataset.type = columns[i].type; // stocke le type en mémoire HTML
    headerRow.appendChild(th);
  }
  thead.appendChild(headerRow);
}
