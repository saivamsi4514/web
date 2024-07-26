<!DOCTYPE html>
<html>

<head>
     <title>Form fillup</title> 
     <link rel="stylesheet" type="text/css" href="style1.css">
     
</head>

<body>
     <form action="formfill_check.php" method="post" enctype="multipart/form-data">
          <h2>Form fillup For Diabetes</h2>
          <?php if (isset($_GET['error'])) { ?>
               <p class="error"><?php echo $_GET['error']; ?></p>
          <?php } ?>
          <?php if (isset($_GET['success'])) { ?>
               <p class="success"><?php echo $_GET['success']; ?></p>
          <?php } ?>
          <label for="age">Age:</label>
          <input type="number" id="age" name="age" placeholder="Enter your age"><br>

          <label for="glucose">Glucose Level:</label>
          <input type="number" id="glucose" name="glucose" placeholder="Enter your glucose level"><br>

          <label for="insulin">Insulin Level:</label>
          <input type="number" id="insulin" name="insulin" placeholder="Enter your insulin level"><br>

          <label for="bmi">BMI (Body Mass Index):</label>
          <input type="number" id="bmi" name="bmi" step="0.01" placeholder="Enter your BMI"><br>

          <label for="blood_pressure">Blood Pressure:</label>
          <input type="number" id="blood_pressure" name="blood_pressure" placeholder="Enter your blood pressure"><br>

          <label for="pregnancies">Number of Pregnancies:</label>
          <input type="number" id="pregnancies" name="pregnancies" placeholder="Enter number of pregnancies"><br>

          <label for="dpf">Diabetes Pedigree Function(DPF):</label>
          <input type="number" id="dpf" name="dpf" step="0.001" placeholder="Enter your DPF"><br>

          <label for="skin_thickness">Skin Thickness:</label>
          <input type="number" id="skin_thickness" name="skin_thickness" placeholder="Enter your skin thickness"><br>
          <button type="submit" name="submit" id="submit">submit</button>
          </form>
</body>

</html>