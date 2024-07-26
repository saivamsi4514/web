<html>

<head>
    <title>Sessions with PHP</title>
</head>

<body>
    <?php
    session_start();
    if (isset($_SESSION['counter'])) {
        $_SESSION['counter'] += 1;
    } else {
        $_SESSION['counter'] = 1;
    }
    $msg = "You have visited this page " . $_SESSION['counter'];
    $msg .= "in this session.";
    echo $msg;
    if ($_SESSION['counter'] >= 5) {
        session_destroy();
    }
    ?>

    <script>
        function checkCookie() {
            let uname = getCookie("uname");
            if (uname != "") {
                alert("Welcome again " + uname);
            } else {
                uname = prompt("Please enter your name:", "");
                if (uname != "" && uname != null) {
                    setCookie("uname", uname, 365);
                }
            }
        }

        function setCookie(cname, cvalue, exdays) {
            const d = new Date();
            d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
            let expires = "expires=" + d.toUTCString();
            document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
        }

        function getCookie(cname) {
            let name = cname + "=";
            let decodedCookie = decodeURIComponent(document.cookie);
            let ca = decodedCookie.split(';');
            for (let i = 0; i < ca.length; i++) {
                let c = ca[i];
                while (c.charAt(0) == ' ') {
                    c = c.substring(1);
                }
                if (c.indexOf(name) == 0) {
                    return c.substring(name.length, c.length);
                }
            }
            return "";
        }
    </script>

</body>