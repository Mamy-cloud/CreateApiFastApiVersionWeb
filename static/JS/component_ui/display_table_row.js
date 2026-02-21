// tableRows.js
export function buildTableRows(tbody, data, columns) {
  tbody.innerHTML = "";

  for (let j = 0; j < data.rows.length; j++) {
    const row = document.createElement("tr");

    for (let i = 0; i < columns.length; i++) {
      const td = document.createElement("td");
      td.textContent = data.rows[j][columns[i].name] ?? "null";
      row.appendChild(td);
    }

    tbody.appendChild(row);
  }
}
