document.addEventListener("DOMContentLoaded", function () {

  const confirmButtons = document.getElementsByClassName('confirm');
  const cancelButtons = document.getElementsByClassName('cancel');
  const deleteButtons = document.getElementsByClassName('delete');
  const bookingForm = document.getElementById('bookingForm');


/**
 * Functionality to confirm a booking by clicking confirm button
 */
  for (let button of confirmButtons) {
    button.addEventListener("click", (e) => {

      // get booking id from dataset of button clicked
      let bookingId = button.dataset.booking_id;
      // insert inner text to cancelled booking button
      button.innerText = "Confirmed!";
      // read current URL
      let currentUrl = window.location.href;
      // remove unused part of URL
      newUrl = currentUrl.replace('/all-bookings/', '');
      // redirect to cancel booking URL with booking number as argument
      window.location.href = `${newUrl}/confirm_booking/${bookingId}`;
    });
  }


/**
 * Functionality to cancel a booking by clicking cancel button
 */
    for (let button of cancelButtons) {
      button.addEventListener("click", (e) => {
  
        let bookingId = button.dataset.booking_id;
        button.innerText = "Cancelled!";
        let currentUrl = window.location.href;
        var newUrl = '';
        if (currentUrl.includes('your-bookings')) {
          newUrl = currentUrl.replace('/your-bookings/', '');
        } else {
          newUrl = currentUrl.replace('/all-bookings/', '');
        }
        window.location.href = `${newUrl}/cancel_booking/${bookingId}`;
  
      });
    }


/**
 * Functionality to delete a booking by clicking delete button
 */
  for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {

      let bookingId = button.dataset.booking_id;
      button.innerText = "Deleted!";
      let currentUrl = window.location.href;
      var newUrl = '';
      if (currentUrl.includes('your-bookings')) {
        newUrl = currentUrl.replace('/your-bookings/', '');
      } else {
        newUrl = currentUrl.replace('/all-bookings/', '');
      }
      window.location.href = `${newUrl}/delete_booking/${bookingId}`;
    });
  }

});