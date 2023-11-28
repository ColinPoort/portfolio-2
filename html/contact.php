<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = $_POST['name'];
    $email = $_POST['email'];
    $comment = $_POST['comment'];
    
    $to = "581827@edu.rocmn.nl"; 
    $subject = "New message from your website contact form";
    $message = "Name: $name\nEmail: $email\nMessage: $comment";
    $headers = "From: $email";

    mail($to, $subject, $message, $headers);
    
    
}
?>