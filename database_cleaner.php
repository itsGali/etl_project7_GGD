<?php
$conn_string = "dbname= user= password=";
$dbconn = pg_connect($conn_string) or die("Could not connect");
$stat = pg_connection_status($dbconn);
$sql = "TRUNCATE product_info, product_opinion, pros_cons;";
$result = pg_query($dbconn, $sql);
echo "<br/>Baza wyczyszczona";

?>
