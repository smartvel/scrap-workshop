<html>
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
		<link href="javascript/js/libs/bootstrap/dist/css/bootstrap.min.css" rel="stylesheet" />
		<link href="javascript/css/main.css" rel="stylesheet"/>
	</head>
	<body style="padding-top: 70px; padding-bottom: 70px">
		<nav class='navbar navbar-default navbar-fixed-top'>
			<div class='container'>
				<div class='navbar-header'>
					<a href="#" class="navbar-brand">Scraping Workshop</a>
					<button data-toggle="collapse" class="navbar-toggle" type="button" data-target='.navbar-collapse'>
					<span class="sr-only">Toggle navigation</span>
					<span class="icon-bar"></span>
					<span class="icon-bar"></span>
					<span class="icon-bar"></span>
					</button>
				</div>
				<ul class="nav navbar-nav navbar-collapse collapse">
					<li><a href="example1.html">Ejemplo página estática</a></li>
					<li><a href="#">Ejemplo paginado</a></li>
					<li><a href="auth/example3.html">Ejemplo Authenticate</a></span></li>
                    <li><a href="javascript/example4.html">Ejemplo Javascript</a></li>
				</ul>
			</div>
		</nav>
		<div class="header">
			<h1> Ejemplo con paginado </h1>
		</div>
		<div class="main">
			<div class="container">
				<?php
				$string = file_get_contents("data.json");
				$json_data = json_decode($string, true);
				$page=$_GET["page"];
				$num_pages = ceil(count($json_data['discos'])/3);

				foreach (array_slice($json_data['discos'], ($page % ($num_pages))*3 , 3) as $disco) {
				echo "<div class='content'>
									<div class='row'>
											<div class='disco'>
													<div class='col-md-3'>
															<img src='images/".$disco['image'].".jpeg'>
													</div>
													<div class='col-md-9'>
															<h1 class='titulo'>".$disco['name']."</h1>
															<ul class='list-group'>
																	<li class='list-group-item'><span id='field'>id:</span><span class='id'> ".$disco['id']." </span></li>
																	<li class='list-group-item'><span id='field'>author:</span><span class='author'> ".$disco['author']."  </span></li>
																	<li class='list-group-item'><span id='field'>Spotify-Link:</span> <a class='spotifylink' href='".$disco['uri']."'>Ir a Spotify</a></span></li>
																	<li class='list-group-item'>
																		<span id:'field'> Canciones: </span>";
																		foreach ($disco['tracks'] as $cancion){
																			echo "<div><span class='cancion'>".$cancion."</span></div>";
																		};
															echo "</li>
															</ul>
														</div>
													</div>
											</div>
										</div>";
				};

			echo "<div class='content text-center'>
			<ul class='pagination'>";


			for ($i = 1; $i <= $num_pages; $i++) {
				echo "<li><a class='page' href='example2.php?page=".($i-1)."'>Página".$i."</a></li>";
			};


			?>
			</ul>
			</div>
			</div>
		</div>
</body>
</html>
