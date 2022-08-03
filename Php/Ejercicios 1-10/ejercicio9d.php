<html>
   <head>
      <title>Captura de datos del form</title>
   </head>
   <body>
      <?php
         echo "El nombre ingresado es: ";
         echo $_REQUEST['nombre'];
         echo "<br>";
         echo "La edad es ". $_REQUEST['edad'];
         echo "<br>";
         if ($_REQUEST['edad'] >= 18){
            echo "Es mayor de edad";
         } else {
            echo "Es menor de edad";
         }
      ?>
   </body>
</html>