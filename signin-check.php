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
            header("Location: signin.php?error=User Name is required&$user_data");
            exit();
        } else if (empty($pass)) {
            header("Location: signin.php?error=Password is required&$user_data");
            exit();
        } else {
            $pass = md5($pass);

            $sql = "SELECT uname FROM diabetes_table WHERE uname='$uname' AND  Password = '$pass'";
            $result = mysqli_query($conn, $sql);

            if (mysqli_num_rows($result)>=0) {
                $_SESSION['uname'] = $uname;
                $cookie_name = $uname;
                $cookie_value = $pass;
                setcookie($cookie_name, $cookie_value, time() + (86400 * 30), "/");
                header("Location: http://127.0.0.1:5000/");
                exit();
            } else {
                header("Location: signin.php?error=Username or Password Incorrect");
                exit();
            }
        }
    }
} else {
    header("Location: signin.php");
    exit();
}