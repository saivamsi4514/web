<html>

<head>
    <title>Accessing Cookies with PHP</title>
</head>

<body>
    <?php

    // setcookie("gopal1", "manohar", time() + 1 * 60);
    if (!isset($_COOKIE["gopal1"])) {
        echo "Cookie is not set";
    } else {
        // setcookie("gopal", "John Watkin");
        echo $_COOKIE["gopal1"] . "welcome to our webpage" . "<br />";
    }
    ?>
</body>