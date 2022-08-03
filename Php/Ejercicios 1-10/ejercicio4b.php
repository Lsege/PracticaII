<html>
<head></head>
<body>
<?php
$num=rand(1,100);

if($num > 50){
    echo "Número mayor a 50";
} 
elseif ($num == 50){
    echo "Número igual a 50";
} 
else {
    echo "Número menor a 50";
}
?>
</body>
</html>