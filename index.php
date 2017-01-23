<!doctype html>
<html class="no-js" lang="">

<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <title></title>
    <meta name="description" content="">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <link rel="stylesheet" href="css/bootstrap.min.css">
    <link rel="stylesheet" href="css/main.css">

    <script src="js/vendor/modernizr-2.8.3.min.js"></script>
</head>

<body>

    <div class="container-fluid">
        <h1>ETL</h1>
        <div class="row">
            <div class="col-md-12">
                <a href="#" onClick="location.reload();">Przeładowanie strony</a>
            </div>
        </div>
        <div class="row">
            <div class="col-md-6">
                <div class="input-group">
                    <span class="input-group-addon" id="basic-addon1">ID produktu: </span>
                    <input type="text" id="id-input" class="form-control" placeholder="np. 37164441">
                </div>
            </div>
            <div class="col-md-6">
                <a class="btn btn-success" href="#" role="button" id="e-button">E</a>
                <a class="btn btn-success disabled" href="#" role="button" id="t-button">T</a>
                <a class="btn btn-success disabled" href="#" role="button" id="l-button">L</a>
                <a class="btn btn-primary" href="#" role="button" id="etl-button">ETL</a>
                <a class="btn btn-info disabled" href="#" role="button" id="export-button">Eksport do CSV</a>
                <a class="btn btn-danger" href="#" role="button" id="clear-button">Wyczyść bazę</a>
            </div>
        </div>
        <div class="row">
            <div id="loader-div" class="col-md-12 text-center">
                <img src="img/loader.gif" />
            </div>
        </div>
        <div class="row">
            <div class="col-md-12">
                <div id="product-result">
                </div>
            </div>
        </div>
        <hr/>
        <footer>
            <p>&copy; Mateusz Galant, Adrianna Gałka, Łukasz Doleżałek 2017</p>
        </footer>
        <iframe style="display:none;" id="downloadiframe"></iframe>
    </div>
    <!-- /container -->
    <script src="//ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
    <script>
        window.jQuery || document.write('<script src="js/vendor/jquery-1.11.2.min.js"><\/script>')
    </script>
    <script src="js/vendor/bootstrap.min.js"></script>
    <script src="js/main.js"></script>
</body>

</html>