const express = require('express');
const app = express();

app.use(express.json());

let bookings = [];

app.post('/submit-booking', (req, res) => {
  const booking = req.body;
  bookings.push(booking);
  res.send('Booking submitted successfully!');
});

app.listen(3000, () => {
  console.log('Server is running on port 3000.');
});
