<?php
include "database_conn.php";

session_start();

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    if (isset($_POST["submit"])) {

        function validate($data)
        {
            $data = trim($data);
            $data = stripslashes($data);
            $data = htmlspecialchars($data);
            return $data;
        }

        $uname = validate($_POST['uname']);
        $pass = validate($_POST['password']);

        $user_data = 'uname=' . $uname;


        if (empty($uname)) {
            header("Location: login.php?error=User Name is required&$user_data");
            exit();
        } else if (empty($pass)) {
            header("Location: login.php?error=Password is required&$user_data");
            exit();
        } else {
            $pass = md5($pass);

            $sql = "SELECT uname FROM diabetes_table WHERE uname='$uname' AND  password = '$pass'";
            $result = mysqli_query($conn, $sql);

            if (mysqli_num_rows($result) > 0) {
                $_SESSION['uname'] = $uname;
                $cookie_uname = $uname;
                $cookie_value = $uname;
                //setcookie($cookie_name, $cookie_value, time() + (86400 * 30), "/");
                header("Location: dashboard_1.php");
                exit();
            } else {
                header("Location: login.php?error=Username or Password Incorrect&$user_data");
                exit();
            }
        }
    }
} else {
    header("Location: login.php");
    exit();
}