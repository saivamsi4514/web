<?php

$host= "localhost";
$username1= "root";
$password = "";
$db_name = "web_tech";

$conn = mysqli_connect($host, $username1, $password, $db_name);


if (!$conn) {
	echo "Connection failed!";
}
