<?php
$id = -1;
$csv = false;

if ($_GET) {
    $id = intval($_GET['product_id']);
    if (isset($_GET['csv']))	 {
        $csv = boolval($_GET['csv']);
    }
}

$conn_string = "dbname= user= password=";
$dbconn = pg_connect($conn_string) or die("Could not connect");
$stat = pg_connection_status($dbconn);
echo '<br/>';

if ($id >= 0) {
    $sql = "SELECT * FROM product_info WHERE product_id=".$id.";";
} else {
    $sql = "SELECT * FROM product_info;";
}

$result = pg_query($dbconn, $sql);
$rows = pg_num_rows($result);

if (!$result || $rows == 0) {
    $output = "Brak wyników dla zapytania.\n";
} else
if (!$csv) {
    $output = '<table class="table table-striped"> <thead>
        <tr><th class="col-md-1"> ID </th> <th class="col-md-1"> Marka </th> <th class="col-md-2"> Model </th> <th class ="col-md-1"> Kategoria </th> <th class="col-md-5"> Parametry </th> <th class="col-md-1"> Ocena </th> <th class="col-md-1"> Ilość opinii </th> </tr>  </thead>';
    while ($myrow = pg_fetch_assoc($result)) {
        $output.= '<tbody>';
        $output.= '<tr>'.
        '<td>'.$myrow['product_id'].
        '</td>'.
        '<td>'.$myrow['producer'].
        '</td>'.
        '<td>'.$myrow['model'].
        '</td>'.
        '<td>'.$myrow['category'].
        '</td>'.
        '<td>'.$myrow['extra_info'].
        '</td>'.
        '<td>'.$myrow['review'].
        '</td>'.
        '<td>'.$myrow['reviews_count'].
        '</td>'.
        '</tr>';
        $output.= '</tbody></table>';
    }

    $sql2 = "SELECT * FROM product_opinion WHERE product_id=".$id.
    ";";
    $result2 = pg_query($dbconn, $sql2);
    $rows2 = pg_num_rows($result2);
    if (!$result2 || $rows2 == 0) {
        $output.= "Brak wyników dla zapytania.\n";
    } else {
        $output.= '<table class="table table-striped"> <thead>
            <tr>
            <th class="col-md-1"> ID recenzji </th> <th class= "col-md-1"> Recenzujący </th> <th class="col-md-1"> Ocena </th> <th class="col-md-1"> Podsumowanie </th> <th class="col-md-3"> Zalety </th> <th class="col-md-3"> Wady </th> <th class="col-md-1"> Czas recenzji </th> </tr></thead>';
        $output.= '<tbody>';
        while ($myrow2 = pg_fetch_assoc($result2)) {
            $output.= '<tr>'.
            '<td>'.$myrow2['product_review_id'].
            '</td>'.
            '<td>'.$myrow2['product_reviewer'].
            '</td>';
            $score = $myrow2['product_reviewers_score'];
            $scoreLoop = ceil(substr($myrow2['product_reviewers_score'], 0, 3));
            $score_beautyfied = "";
            for ($x = 1; $x <= $scoreLoop; $x++) {
                $score_beautyfied.= '<span class="glyphicon glyphicon-star" aria-hidden="true"></span>';
            }

            $score_beautyfied.= " ".$score;
            $output.= '<td>'.$score_beautyfied.
            '</td><td>'.$myrow2['product_review_summary'].
            '</td>';
            $sql3 = "SELECT * FROM pros_cons WHERE product_review_id=".$myrow2['product_review_id'].
            ";";
            $result3 = pg_query($dbconn, $sql3);
            $rows3 = pg_num_rows($result3);
            if (!$result3 || $rows3 == 0) {
                $output.= '<td></td>';
                $output.= '<td></td>';
            } else {
                while ($myrow3 = pg_fetch_assoc($result3)) {
                    $output.= '<td>'.substr($myrow3['pros'],6).
                    '</td>';
                    $output.= '<td>'.substr($myrow3['cons'],4).
                    '</td>';
                }
            }

            $output.= '<td>'.$myrow2['product_review_time'].
            '</td>'.
            '</tr>';
        }

        $output.= '</tbody></table>';
    }
} else
if ($csv == true && $result && $rows > 0) {
    $fp = fopen('file.csv', 'w');
    $row = pg_fetch_assoc($result);
    fputcsv($fp, array_values($row));
    fclose($fp);
    $output = "Zapisano do pliku";
}

echo $output; ?>
