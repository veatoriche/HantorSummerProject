<?php
	$file = fopen('buffer/output','r');
	$text = fread($file,100);
	fclose($file);
	echo $text;
?>
