<?php
$row = 1;
if (($handle = fopen("leitura.csv", "r")) !== FALSE) {
    while (($data = fgetcsv($handle, 1000, ";")) !== FALSE) {
        $num = count($data);
        //echo "<p> $num campos na linha $row: <br /></p>\n";
        //$row++;
        for ($c=0; $c < $num; $c++) {
            echo $data[$c] . ";";
        }
    }
    fclose($handle);
}
?>
