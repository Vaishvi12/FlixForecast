function submitForm() {
    // Get input values
    var movieName = document.getElementById('input-1').value;
    var directorName = document.getElementById('input-2').value;
    var actorName = document.getElementById('input-3').value;

    // Validation regex (allowing only letters and spaces)
    var nameRegex = /^[A-Za-z\s]+$/;

    // Perform validation
    if (!nameRegex.test(movieName.trim())) {
      alert('Please enter a valid name for the movie (only letters and spaces).');
      return;
    }

    if (!nameRegex.test(directorName.trim())) {
      alert('Please enter a valid name for the director (only letters and spaces).');
      return;
    }

    if (!nameRegex.test(actorName.trim())) {
      alert('Please enter a valid name for the actor (only letters and spaces).');
      return;
    }

    // If all validations pass, you can proceed with form submission
    alert('Form submitted successfully!');
    // Uncomment the following line to submit the form
    // document.getElementById('yourFormId').submit();
  }
    
