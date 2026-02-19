// post_column.js
import { getColumnsJSON, showPreview } from "../component_ui/previsualisation_column.js";

// Récupère le nom de la table depuis l'URL
const addColumntableName = window.location.pathname.split("/").pop();

document.getElementById("validateColumnsBtn").addEventListener("click", async () => {
  // Récupérer les colonnes saisies
  const columnsToAdd = getColumnsJSON();

  if (columnsToAdd.length === 0) {
    alert("Aucune colonne valide à ajouter !");
    return;
  }

  // Affiche la prévisualisation
  showPreview(columnsToAdd);
  console.log(columnsToAdd)
  try {
    const response = await fetch(`/admin/tables/${addColumntableName}/add-columns`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ columns: columnsToAdd })
    });

    if (!response.ok) throw new Error("Erreur serveur : " + response.status);

    const result = await response.json();
    alert("✅ Colonnes ajoutées avec succès !");
    window.location.reload();
  } catch (err) {
    alert("❌ Erreur : " + err.message);
    console.error(err);
  }
});
