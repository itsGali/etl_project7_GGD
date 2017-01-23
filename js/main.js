$("#e-button").click(function() {
    $id = $("#id-input").val();
    $('#loader-div').show();
    getE($id);
});


$("#t-button").click(function() {
    $('#product-result').html("");
    $id = $("#id-input").val();
    $('#loader-div').show();
    getT($id);
});



$("#l-button").click(function() {
    $('#product-result').html("");
    $id = $("#id-input").val();
    $('#loader-div').show();
    getL($id);
});


$("#etl-button").click(function() {
    $('#product-result').html("");
    $id = $("#id-input").val();
    $('#loader-div').show();
    getETL($id);
});



$("#export-button").click(function() {
    $id = $("#id-input").val();
    $('#loader-div').show();
    saveCSV($id);
});

$("#clear-button").click(function() {
    $id = $("#id-input").val();
    $('#loader-div').show();
    clearBase();
});




function getE($id) {
    $.ajax({
        url: 'python_executor.php',
        data: "csv=0&product_id=" + $id,
        error: function(error) {
            $('#product-result').html(data);
            $('#loader-div').hide();
        },
        success: function(data)
            {
                $('#product-result').html(data);
                $('#loader-div').hide();
                setEVisibility(false);
                setTVisibility(true);
                setLVisibility(false);
                setETLVisibility(false);
                setClearVisibility(true);
            }
    });
}

function getT($id) {
    $.ajax({
        url: 'python_executor.php',
	data: 'transform=1',
        error: function(error) {
            $('#product-result').html(error);
            $('#loader-div').hide();
        },
        success: function(data)
            {
                $('#product-result').html(data);
                $('#loader-div').hide();
                setEVisibility(false);
                setTVisibility(false);
                setLVisibility(true);
                setETLVisibility(false);
                setClearVisibility(true);
            }
    });
}


function getL($id) {
    $.ajax({
        url: 'connector.php',
        data: "csv=0&product_id=" + $id,
        error: function(error) {
            $('#product-result').html(error);
            $('#loader-div').hide();
        },
        success: function(data)
            {
                $('#product-result').html(data);
                $('#loader-div').hide();
                setEVisibility(false);
                setTVisibility(false);
                setLVisibility(false);
                setETLVisibility(false);
                setEexportVisibility(true);
                setClearVisibility(true);
            }
    });
}


function getETL($id) {
    $.ajax({
        url: 'python_executor.php',
        data: "etl=1&product_id=" + $id,
        error: function(error) {
            $('#product-result').html(error);
            $('#loader-div').hide();
        },
        success: function(data)
            {
				getL($id);
            }
    });
}

function clearBase() {
    $.ajax({
        url: 'database_cleaner.php',
        error: function(error) {
            $('#product-result').html(data);
            $('#loader-div').hide();
        },
        success: function(data)
            {
                $('#product-result').html(data);
                $('#loader-div').hide();
                setEVisibility(false);
                setTVisibility(false);
                setLVisibility(false);
                setETLVisibility(false);
                setClearVisibility(true);
            }
    });
}

function saveCSV($id) {
    $.ajax({
        url: 'python_executor.php',
        error: function(error) {
            $('#product-result').html(data);
            $('#loader-div').hide();
        },
        success: function(data)
            {
                $('#product-result').html(data);
                $('#loader-div').hide();
                setEVisibility(false);
                setTVisibility(false);
                setLVisibility(false);
                setETLVisibility(false);
                setClearVisibility(true);
                $("#downloadiframe").attr('src', 'etl_csv.csv');
            }
    });
}


function setEVisibility($visible) {
    if ($visible) {
        if ($("#e-button").hasClass("disabled")) {
            $('#e-button').removeClass("disabled");
        }
    } else {
        if (!$("#e-button").hasClass("disabled")) {
            $('#e-button').addClass("disabled");
        }
    }
}

function setTVisibility($visible) {
    if ($visible) {
        if ($("#t-button").hasClass("disabled")) {
            $('#t-button').removeClass("disabled");
        }
    } else {
        if (!$("#t-button").hasClass("disabled")) {
            $('#t-button').addClass("disabled");
        }
    }

}

function setLVisibility($visible) {

    if ($visible) {
        if ($("#l-button").hasClass("disabled")) {
            $('#l-button').removeClass("disabled");
        }
    } else {
        if (!$("#l-button").hasClass("disabled")) {
            $('#l-button').addClass("disabled");
        }
    }
}

function setETLVisibility($visible) {

    if ($visible) {
        if ($("#etl-button").hasClass("disabled")) {
            $('#etl-button').removeClass("disabled");
        }
    } else {
        if (!$("#etl-button").hasClass("disabled")) {
            $('#etl-button').addClass("disabled");
        }
    }
}

function setClearVisibility($visible) {

    if ($visible) {
        if ($("#clear-button").hasClass("disabled")) {
            $('#clear-button').removeClass("disabled");
        }
    } else {
        if (!$("#clear-button").hasClass("disabled")) {
            $('#clear-button').addClass("disabled");
        }
    }
}

function setEexportVisibility($visible) {

    if ($visible) {
        if ($("#export-button").hasClass("disabled")) {
            $('#export-button').removeClass("disabled");
        }
    } else {
        if (!$("#export-button").hasClass("disabled")) {
            $('#export-button').addClass("disabled");
        }
    }
}
