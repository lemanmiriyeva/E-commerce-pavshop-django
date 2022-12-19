// // With Fetch API: 
const form = document.getElementById('subscription-form')
form.addEventListener('submit', function(event){
  event.preventDefault();
  let email = document.getElementById('subscription-email')
  console.log(email.value);

  const data = { email: email.value };

  fetch('http://localhost:8000/en/api/subscribe/', {
    method: 'POST', // or 'PUT'
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
  })
    .then((response) => response.json())
    .then((data) => {
      console.log('Success:', data);
    })
    .catch((error) => {
      console.error('Error:', error);
    });
})




// With Axios:  Axios is a Javascript library used to make HTTP requests
// const form = document.getElementById('subscription-form')        // selecting the form
// form.addEventListener('submit', function(event) { // 1
//     event.preventDefault()
    
//     let data = new FormData(); // 2. Creates a new form in JavaScript
    
//     data.append("email", document.getElementById('subscription-email').value)  
//     data.append("csrfmiddlewaretoken", '{{csrf_token}}') // 3.Adds a CRSF token. If we do not include this we get a 403 forbidden response and we won’t be able to submit the form data.
    
//     axios.post('api/subscribe/', data) // 4.Here we use axios.post method to submit form data.
//      .then(res => alert("Form Submitted")) // 5
//      .catch(errors => alert("Error occured! Please enter valid email address!")) // 6

// })
