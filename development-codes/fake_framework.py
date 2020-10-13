def src_header(title, ancestors, open_catalog):
    ret =  src_header = """<!DOCTYPE html>
<html>
<head>
    <title>{0}</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="//cdnjs.cloudflare.com/ajax/libs/bootswatch/3.3.7/cosmo/bootstrap.css">
    <link rel="stylesheet" href="static/pangeo-style.css">

</head>
<body>

<div id="navbar" class="navbar navbar-inverse navbar-default navbar-fixed-top">
    <div class="container">
        <div class="navbar-header">
            <!-- .btn-navbar is used as the toggle for collapsed navbar content -->
            <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".nav-collapse">
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
            </button>
            <a class="navbar-brand" href="/firstJekyll/">
                <span><img src="img/cola.gif"></span>
                COLA Catalog</a>
            <span class="navbar-text navbar-version pull-left"><b></b></span>
        </div>
        <div class="collapse navbar-collapse nav-collapse">
            <ul class="nav navbar-nav">
               <!-- <li><a href="https://medium.com/pangeo">Blog</a></li>
                <li><a href="https://discourse.pangeo.io">Forum</a></li>  -->
            </ul>
        </div>
    </div>
</div>


<main role="main" class="container">
    <h1>{1}</h1>
    <div>
        <ol class="breadcrumb">

            <li><a href="main">main</a></li>
			{2}

            <li class="active">{3}</li>

        </ol>
    </div>
    <div class="catalog">

        <h2> sea surface temperature </h2>
        

        <h3>Load in Python</h3>
        <pre><code class="language-python">from intake import open_catalog<br>
cat = open_catalog("{4}")
list(cat)</code></pre>




        <h3>Datasets</h3>
        <div class="list-group">
        
        <!--qazwsxxswzaq-->







        </div>

    </div>
</main>



<script src="//cdnjs.cloudflare.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
<script src="//cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.7/js/bootstrap.min.js"></script>
</body>
</html>
""".format(title, title, ancestors, title, open_catalog)
    return ret
