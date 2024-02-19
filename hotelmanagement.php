<?php
$servername = "localhost";
$username = "username";
$password = "password";
$dbname = "hotel_db";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

$sql = "INSERT INTO bookings (room_number, guest_name, check_in_date, check_out_date)
VALUES ('101', 'John Doe', '2024-02-20', '2024-02-25')";

if ($conn->query($sql) === TRUE) {
  echo "New record created successfully";
} else {
  echo "Error: " . $sql . "<br>" . $conn->error;
}

$conn->close();
?>
