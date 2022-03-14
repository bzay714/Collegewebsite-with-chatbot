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

    }).then(msg => alert("The email successfully sent"))
})