<html>
    <head>
        <title>Problema</title>
    </head>
    <body>
        <?php
            echo $_REQUEST['nombre']. "<br>";
            if (isset($_REQUEST['fubol'])){
                echo "Juega futbol";
                echo "<br>";
            }
            if (isset($_REQUEST['basque'])){
                echo "Juega Basquet";
                echo "<br>";
            }
            if (isset($_REQUEST['tennis'])){
                echo "Juega tennis";
                echo "<br>";
            }
            if (isset($_REQUEST['voley'])){
                echo "Juega Voley";
                echo "<br>";
            }            
        ?>
    </body>
</html>