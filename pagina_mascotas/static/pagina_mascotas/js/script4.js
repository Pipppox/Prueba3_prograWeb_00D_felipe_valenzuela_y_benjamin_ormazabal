document.addEventListener("DOMContentLoaded", function() {
    const tipoMascota = document.getElementById("tipoMascota");
    const alimento = document.getElementById("alimento");
    const cantidad = document.getElementById("cantidad");
    const dietaLista = document.getElementById("dietaLista");
  
    window.agregarAlimento = function() {
      if (tipoMascota.value === "" || alimento.value === "" || cantidad.value === "") {
        alert("Por favor, completa todos los campos.");
        return;
      }
  
      const listItem = document.createElement("li");
      listItem.className = "list-group-item d-flex justify-content-between align-items-center";
      listItem.textContent = `${alimento.options[alimento.selectedIndex].text} (${cantidad.value} gramos)`;
  
      const removeButton = document.createElement("button");
      removeButton.className = "btn btn-danger btn-sm";
      removeButton.textContent = "Eliminar";
      removeButton.onclick = function() {
        dietaLista.removeChild(listItem);
      };
  
      listItem.appendChild(removeButton);
      dietaLista.appendChild(listItem);
  
      alimento.value = "";
      cantidad.value = "";
    };
  });