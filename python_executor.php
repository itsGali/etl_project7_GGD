<?php

$id=-1;
if ($_GET) {
	if($_GET['etl']){
		$id = intval($_GET['product_id']);
		$output = passthru("python extract_class.py $id");
		$output = passthru("python transform_class.py $id");
	}
	 else if($_GET['product_id']){
		$id = intval($_GET['product_id']);
		$output = passthru("python extract_class.py $id");
	}
	else if($_GET['transform']){
	$output = passthru("python transform_class.py");
	}
}
else{
	$output = passthru("python csv_getter.py");
}
?>
