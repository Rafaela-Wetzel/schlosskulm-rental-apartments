document.addEventListener("DOMContentLoaded", function () {

  const confirmButtons = document.getElementsByClassName('confirm');
  const cancelButtons = document.getElementsByClassName('cancel');
  const deleteButtons = document.getElementsByClassName('delete');
  const bookingForm = document.getElementById('bookingForm');


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


  for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {

      // get booking id from dataset of button clicked
      let bookingId = button.dataset.booking_id;
      // insert inner text to cancelled booking button
      button.innerText = "Deleted!";
      console.log("Hi")
      // read current URL
      let currentUrl = window.location.href;
      var newUrl = '';
      // remove unused part of URL
      if (currentUrl.includes('your-bookings')) {
        newUrl = currentUrl.replace('/your-bookings/', '');
      } else {
        newUrl = currentUrl.replace('/all-bookings/', '');
      }
      // redirect to cancel booking URL with booking number as argument
      window.location.href = `${newUrl}/delete_booking/${bookingId}`;
    });
  }


  for (let button of cancelButtons) {
    button.addEventListener("click", (e) => {

      // get booking id from dataset of button clicked
      let bookingId = button.dataset.booking_id;
      // insert inner text to cancelled booking button
      button.innerText = "Cancelled!";
      // read current URL
      let currentUrl = window.location.href;
      var newUrl = '';
      // remove unused part of URL
      if (currentUrl.includes('your-bookings')) {
        newUrl = currentUrl.replace('/your-bookings/', '');
      } else {
        newUrl = currentUrl.replace('/all-bookings/', '');
      }
      // redirect to cancel booking URL with booking number as argument
      window.location.href = `${newUrl}/cancel_booking/${bookingId}`;

    });
  }

});