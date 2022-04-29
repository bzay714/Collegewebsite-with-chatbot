
var modal = document.getElementById("myModal");
var modal2 = document.getElementById("myModal2");
var span = document.getElementsByClassName("close")[0];
var span1 = document.getElementsByClassName("close1")[0];
const btn = document.querySelector('button')
const inputs = document.querySelector('form')
btn.addEventListener('click', () => {
    Email.send({
        Host: "smtp.mailtrap.io",
        Username: "49b4c5d01bfaee",
        Password: "df27735c937c97",
        To: "714bzaylama@gmail.com",
        From: inputs.elements['email'].value,
        Subject: "Contact Us Query",
        Body: inputs.elements['message'].value + "<br>" +"<br>" + "Regards,"  + "<br>" + inputs.elements['name'].value
    }).then(msg => {
        if (msg=="OK"){
            modal.style.display = "block";
        }else{
            modal2.style.display = "block";
        }
    })
})


span.onclick = function() {
    modal.style.display = "none";
  }

  
span1.onclick = function() {
    modal2.style.display = "none";
  }

window.onclick = function(event) {
    if (event.target == modal) {
      modal.style.display = "none";
    }
  }