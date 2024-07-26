<!DOCTYPE html>
<html>

<head>
    <title>SIGN IN</title>
    <link rel="stylesheet" type="text/css" href="style1.css">
</head>

<body>
    <form action="signin-check.php" method="post" enctype="multipart/form-data">
        <h2>SIGN IN</h2>
        <?php if (isset($_GET['error'])) { ?>
            <p class="error"><?php echo $_GET['error']; ?></p>
        <?php } ?>

        <?php if (isset($_GET['success'])) { ?>
            <p class="success"><?php echo $_GET['success']; ?></p>
        <?php } ?>

        <label>User Name</label>
        <?php if (isset($_GET['uname'])) { ?>
            <input type="text" name="uname" placeholder="User Name" value="<?php echo $_GET['uname']; ?>"><br>
        <?php } else { ?>
            <input type="text" name="uname" placeholder="User Name"><br>
        <?php } ?>


        <label>Password</label>
        <input type="password" name="password" placeholder="Password"><br>

        <a href="register.php">Create a new account</a>

        <button type="submit" name="submit">Sign In</button>
    </form>
</body>

</html>