<html>
    <head>
        <title>Problema</title>
    </head>
    <body> 
        <?php
            if ($_REQUEST['operacion']=="rico"){
                echo "La persona ". $_REQUEST['valor1']. " debe pagar impuesos a las ganancias";
            }  
            
            if($_REQUEST['operacion']=="pobre"){
                echo "aaaaaaaaaaa";
            }
            
        ?>
    </body>
</html>