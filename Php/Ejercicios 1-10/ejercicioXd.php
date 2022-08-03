<html>
    <head>
        <title>Problema</title>
    </head>
    <body>
        <?php
            if ($_REQUEST['estudios']=="sin estudios"){
                echo "La persona <b>". $_REQUEST['nombre']. "</b> no tiene estudios";
            } else{
                if ($_REQUEST['estudios'] == "Primaria"){
                    echo "La persona <b>". $_REQUEST['nombre']. "</b> terminó la primaria";
                } else {
                    if($_REQUEST['estudios'] == "Secundaria"){
                         echo "La persona <b>". $_REQUEST['nombre']. "</b> terminó la secundaria";
                    }
                }
            }  
        ?>
    </body>
</html>