<?php

if ($_SERVER["REQUEST_METHOD"] !== "POST") {
    http_response_code(405);
    exit("Nothing Fun Here For You, Leave.");
}

$data = file_get_contents("php://input");

if ($data === false || $data === "") {
    http_response_code(400);
    exit("No data received");
}

echo "Received key:\n";
echo $data;