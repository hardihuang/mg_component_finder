<?php
	$id = strip_tags($_GET['id']);
	system("gpio -g write 4 1");
	exec('sudo python rotate_servo.py '.$id);
?>