const pathParts = window.location.pathname.split("/");
const oldName = pathParts[pathParts.length - 1]; // récupère {table_name}

document.getElementById("renameTableForm").addEventListener("submit", async (e) => {
  e.preventDefault();

  const newName = document.getElementById("newName").value;

  try {
    const response = await fetch(`/admin/tables/${oldName}/rename`, {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({ new_name: newName })
    });

    if (!response.ok) {
      throw new Error("Erreur serveur: " + response.status);
    }

    const result = await response.json();
    alert("✅ " + result.message);

    // Recharge l’interface admin/tables
    window.location.href = "/admin/" + newName;

  } catch (error) {
    alert("❌ Erreur: " + error.message);
    console.error(error);
  }
});
