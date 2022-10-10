// edit Customer
function editCustomer(id){
    var id = id
    var username = document.getElementById("username-" + id).innerText;
    var phone = document.getElementById("phone-" + id).innerText;
    var email = document.getElementById("email-" + id).innerText;
    var address = document.getElementById("address-" + id).innerText;
    var wallet_balance = document.getElementById("wallet_balance-" + id).getAttribute("data-id");
    var rating = document.getElementById("rating-" + id).innerText;

    document.getElementById('username').value = username;
    document.getElementById("phone").value = phone;
    document.getElementById("email").value = email;
    document.getElementById("address").value = address;
    document.getElementById("rating").selectedIndex = rating - 1;
    document.getElementById("wallet_balance").value = wallet_balance;
    document.getElementById("uid").value = id;
}
function sweetDelete(id) {
    console.log("id" + id)
    var id = id;
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    Swal.fire({
      title: "Are you sure?",
      text: "You won't be able to revert this!",
      icon: "warning",
      showCancelButton: !0,
      confirmButtonText: "Yes, delete it!",
      cancelButtonText: "No, cancel!",
      confirmButtonClass: "btn btn-success mt-2",
      cancelButtonClass: "btn btn-danger ms-2 mt-2",
      buttonsStyling: !1,
    }).then(function (t) {
        if (t.isConfirmed){
            Swal.fire({
                title: "Deleted!",
                text: "Your record has been deleted.",
                icon: "success",
              });
                const xhttp = new XMLHttpRequest();
                const data = new FormData();
                data.append('id', id);
                data.append('deleteCustomer','deleteCustomer');
                const header =  "X-CSRFToken"
                xhttp.open('POST','/ecommerce/customers');
                xhttp.setRequestHeader(header, csrftoken);
                xhttp.send(data);
                xhttp.onload = () => {
                    window.location.reload();
                };
        }
        else {
            Swal.fire({
                title: "Cancelled",
                text: "Your imaginary file is safe :)",
                icon: "error",
              });
        }
    });
}