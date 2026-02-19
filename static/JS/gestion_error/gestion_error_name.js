// Injection du bloc HTML des règles dans tous les éléments ayant la classe "verification_name"
document.querySelectorAll(".verification_name").forEach(container => {
  container.innerHTML = `
    <div>
      <input type="checkbox" class="rule1">
      <label class="label1">Minuscules uniquement</label><br>

      <input type="checkbox" class="rule2">
      <label class="label2">Pas d’accents, pas d’espaces, pas d’apostrophes, pas de caractère spécial</label><br>

      <input type="checkbox" class="rule3">
      <label class="label3">Pas de chiffre au début mais on peut les mettre après une lettre</label><br>
    </div>
  `;
});


// gestion_error_name.js
export function verifierNom(input) {
  const rule1 = /^[a-z0-9_]+$/.test(input);
  const rule2 = /^[a-z0-9_]+$/.test(input);
  const rule3 = /^[a-z][a-z0-9_]*$/.test(input);

  return { rule1, rule2, rule3, isValid: rule1 && rule2 && rule3 };
}

export function afficherResultats(resultats, container) {
  if (!container) return;

  const rule1 = container.querySelector(".rule1");
  const label1 = container.querySelector(".label1");
  if (rule1 && label1) {
    rule1.checked = resultats.rule1;
    label1.style.color = resultats.rule1 ? "green" : "red";
  }

  const rule2 = container.querySelector(".rule2");
  const label2 = container.querySelector(".label2");
  if (rule2 && label2) {
    rule2.checked = resultats.rule2;
    label2.style.color = resultats.rule2 ? "green" : "red";
  }

  const rule3 = container.querySelector(".rule3");
  const label3 = container.querySelector(".label3");
  if (rule3 && label3) {
    rule3.checked = resultats.rule3;
    label3.style.color = resultats.rule3 ? "green" : "red";
  }
}

