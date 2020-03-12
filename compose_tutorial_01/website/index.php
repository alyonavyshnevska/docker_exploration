<html>
    <head>
        <title> Service </title>
    </head>

    <body>
        <h1>Below are some example servicec</h1>
        <ul>
            <?php
                $json = file_get_contents('http://product-service/');
                $obj = json_decode($json);

                $products = $obj->prodcuts;
                foreach ($products as $product) {
                    echo "<li>$product</li>";
                }
            ?>
        </ul>
    </body>
</html>