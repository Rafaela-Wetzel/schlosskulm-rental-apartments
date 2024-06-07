document.addEventListener("DOMContentLoaded", function(){  
  
  const confirmButton = document.getElementById('btn-card-confirm');
  const cancelButtons = document.getElementsByClassName('cancel');
  const deleteButton = document.getElementById('btn-card-delete');
  const bookingForm = document.getElementById('bookingForm'); 

  for (let button of cancelButtons) {
      button.addEventListener("click", (e) => {
      
      // get booking id from dataset of button clicked
      let bookingId = button.dataset.booking_id;
      // insert inner text to cancelled booking button
      button.innerText = "Cancelled!";
      // read current URL
      let currentUrl = window.location.href;
      // remove unused part of URL
      let newUrl = currentUrl.replace('/your-bookings/', '');
      // redirect to cancel booking URL with booking number as argument
      window.location.href = `${newUrl}/cancel_booking/${bookingId}`;

    });
  }

  confirmButton.addEventListener("click", (e) => {
    
    // get booking id from dataset of button clicked
    let bookingId = button.dataset.booking_id;
    // insert inner text to cancelled booking button
    button.innerText = "Confirmed!";
    console.log("Check!")
    // read current URL
    let currentUrl = window.location.href;
    // remove unused part of URL
    let newUrl = currentUrl.replace('/your-bookings/', '');
    // redirect to cancel booking URL with booking number as argument
    window.location.href = `${newUrl}/confirm_booking/${bookingId}`;

  });





});