<?php
    $ressource = fopen('.passwd', 'rb');
    echo fread($ressource, filesize('test.txt'));
?>