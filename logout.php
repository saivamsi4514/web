<?php

session_start();
if (!isset($_SESSION['uname'])) {
    header("Location: signin.php");
    exit();
}
session_destroy();
header("Location: signin.php");
exit();
?>
