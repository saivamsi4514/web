<?php 
// Include database connection code if needed
include "database_conn.php";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    if (isset($_POST["submit"])) {

        // Function to validate form data
        function validate($data) {
            $data = trim($data);
            $data = stripslashes($data);
            $data = htmlspecialchars($data);
            return $data;
        }

        // Validate and sanitize form data
        $age = validate($_POST['age']);
        $glucose = validate($_POST['glucose']);
        $insulin = validate($_POST['insulin']);
        $BMI = validate($_POST['bmi']);
        $blood_pressure = validate($_POST['blood_pressure']);
        $pregnancy = validate($_POST['pregnancies']);
        $skin_thickness = validate($_POST['skin_thickness']);
        $DPF = validate($_POST['dpf']);

        // Check if any form field is empty
        if (empty($age)) {
            header("Location: formfill.php?error=age are required");
            exit();
        }
        else if(empty($glucose)){
            header("Location: formfill.php?error=glucose are required");
            exit();
        }
        else if(empty($insulin)){
            header("Location: formfill.php?error=insulin are required");
            exit();
        }
        else if(empty($BMI)){
            header("Location: formfill.php?error=BMI are required");
            exit();
        }
        else if(empty($blood_pressure)){
            header("Location: formfill.php?error=blood_pressure are required");
            exit();
        }
        else if(empty($pregnancy)){
            header("Location: formfill.php?error=pregnancy are required");
            exit();
        }
        else if(empty($skin_thickness)){
            header("Location: formfill.php?error=skin_thickness are required");
            exit();
        }
        else if(empty($DPF)){
            header("Location: formfill.php?error=DPF are required");
            exit();
        }
        
        else {
            // Prepare POST data
            $post_data = http_build_query([
                'age' => $age,
                'glucose' => $glucose,
                'insulin' => $insulin,
                'bmi' => $BMI,
                'blood_pressure' => $blood_pressure,
                'pregnancies' => $pregnancy,
                'skin_thickness' => $skin_thickness,
                'dpf' => $DPF
            ]);

            // Set cURL options
            $curl = curl_init();
            curl_setopt_array($curl, array(
                CURLOPT_URL => "http://localhost:5000/predict",
                CURLOPT_RETURNTRANSFER => true,
                CURLOPT_POST => true,
                CURLOPT_POSTFIELDS => $post_data
            ));

            // Execute cURL request
            $response = curl_exec($curl);

            // Close cURL session
            curl_close($curl);

            // Check if request was successful
            if ($response === false) {
                echo "Error: Unable to retrieve data from Flask application";
            } else {
                echo " " . $response;
            }
        }
    }
} else {
    header("Location: formfill.php");
    exit();
}
?>
