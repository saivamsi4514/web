<!DOCTYPE html>
<html>

<head>
     <title>SIGN UP</title>
     <link rel="stylesheet" type="text/css" href="style1.css">
     <style>
</style>
</head>

<body >
     
     <form action="register_check.php" method="post" enctype="multipart/form-data">
          <h2>SIGN UP</h2>
          <?php if (isset($_GET['error'])) { ?>
               <p class="error"><?php echo $_GET['error']; ?></p>
          <?php } ?>

          <?php if (isset($_GET['success'])) { ?>
               <p class="success"><?php echo $_GET['success']; ?></p>
          <?php } ?>

          <label>Name</label>
          <?php if (isset($_GET['name'])) { ?>
               <input type="text" name="name" placeholder="Name" value="<?php echo $_GET['name']; ?>"><br>
          <?php } else { ?>
               <input type="text" name="name" placeholder="Name"><br>
          <?php } ?>

          <label>User Name</label>
          <?php if (isset($_GET['uname'])) { ?>
               <input type="text" name="uname" placeholder="User Name" value="<?php echo $_GET['uname']; ?>"><br>
          <?php } else { ?>
               <input type="text" name="uname" placeholder="User Name"><br>
          <?php } ?>


          <label>Password</label>
          <input type="password" name="password" placeholder="Password"><br> 

          <label>Confirm Password</label>
          <input type="password" name="re_password" placeholder="Re_Password"><br>
     
         
          <a href="login.php">Already have an account</a>


          <button type="submit" name="submit">Sign Up</button>
     </form>
</body>

</html>