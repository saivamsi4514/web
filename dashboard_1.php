<?php

session_start();

// if (!isset($_COOKIE[$cookie_name])) {
//     header("Location: signin.php");
//     exit();
// }
if (!isset($_SESSION['uname'])) {
    header("Location: login.php");
    exit();
}

?>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard</title>
    <link rel="stylesheet" type="text/css" href="style1.css">
</head>

<body>
    <?php
    // if(isset($_COOKIE[$cookie_name])){
    if(isset($_SESSION['uname'])){
        ?>
        <h1>Welcome to dashboard <?php echo $_SESSION['uname']; ?></h1><?php
    }
    ?>
        
    <br>
    <button type="button" onclick="location.href='logout.php'" class="btn btn-dark">Logout</button>
</body>

</html>