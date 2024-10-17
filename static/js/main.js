document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("signup-form");
    const userTable = document.getElementById("user-table");
    const tableBody = userTable.querySelector("tbody");

    
    form.addEventListener("submit", function (event) {
      event.preventDefault();
  
      const email = document.getElementById("floatingEmail").value;
      const surname = document.getElementById("floatingSurname").value;
      const name = document.getElementById("floatingName").value;
      const patronymic = document.getElementById("floatingPatronymic").value;
      const birthdate = document.getElementById("floatingBirthdate").value;
      const phone = document.getElementById("floatingPhone").value;
      const group = document.getElementById("group").value;
      const fileUpload = document.getElementById("file-upload").files[0];
  
      if (
        email &&
        surname &&
        name &&
        patronymic &&
        birthdate &&
        phone &&
        group &&
        fileUpload
      ) {
        const newRow = document.createElement("tr");
  
        newRow.innerHTML = `
          <td>${email}</td>
          <td>${surname}</td>
          <td>${name}</td>
          <td>${patronymic}</td>
          <td>${birthdate}</td>
          <td>${phone}</td>
          <td>${group}</td>
          <td>${fileUpload.name}</td>
        `;
  
        tableBody.appendChild(newRow);
        userTable.style.display = "block";  
  
        form.reset();
      } else {
        alert("Please fill in all fields.");
      }
    });
  });
  