<?php
    $name = $_POST["nameField"]; //You have to get the form data
    $attendance = $_POST["attendanceField"];
    $guests = $_POST["guestField"];
    $file = fopen('database.txt', 'w+'); //Open your .txt file
    ftruncate($file, 0); //Clear the file to 0bit
    $content = $name. PHP_EOL .$attendance. PHP_EOL .$guests;
    fwrite($file , $content); //Now lets write it in there
    fclose($file ); //Finally close our .txt
    die(header("Location: ".$_SERVER["HTTP_REFERER"]));
?>