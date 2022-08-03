<html>
<head>
<title>Problema</title>
</head>
<body>
<?php
$valor=rand(1,50);
$inicio=1;
echo "El valor random generado es ". $valor;
echo "<br>";
while($inicio<=$valor)
{
 echo $inicio;
 echo "<br>";
 $inicio++;
}
?>
</body>
</html>