window.onload = function () {

  const confirmButtons = document.getElementById('btn-card-confirm');
  const cancelButtons = document.getElementsByClassName('btn-card-cancel');
  const deleteButtons = document.getElementById('btn-card-delete');
  const bookingForm = document.getElementById('bookingForm');

  /**
   * Initializes cancel functionality for the provided edit buttons.
   * 
   * For each button in the `cancelButtons` collection:
   * - Retrieves the associated booking's ID upon click.
   * - Updates the cancel button's text to "Cancelled!".
   * - Sets the form's action attribute to the `cancel_booking/{bookingId}` endpoint.
   */

  for (let button of cancelButtons) {
    button.addEventListener("click", (e) => {
      let bookingId = e.target.getAttribute("booking_id");
      cancelButtons.innerText = "Cancelled!";
      bookingForm.setAttribute("action", `${bookingId}`);
    });
  }

}