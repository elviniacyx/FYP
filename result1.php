<!DOCTYPE HTML>

<html>
	<head>
		<title>General Search Result</title>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
		<link rel="stylesheet" href="assets/css/main.css" />
		<noscript><link rel="stylesheet" href="assets/css/noscript.css" /></noscript>


		<meta charset="utf-8">
	  <meta http-equiv="X-UA-Compatible" content="IE=edge">

	  <!-- Custom fonts for this template -->
	  <link href="vendor/fontawesome-free/css/all.min.css" rel="stylesheet" type="text/css">
	  <link href="https://fonts.googleapis.com/css?family=Nunito:200,200i,300,300i,400,400i,600,600i,700,700i,800,800i,900,900i" rel="stylesheet">

	  <!-- Custom styles for this template -->
	  <link href="css/sb-admin-2.min.css" rel="stylesheet">

	  <!-- Custom styles for this page -->
	  <link href="vendor/datatables/dataTables.bootstrap4.min.css" rel="stylesheet">


	</head>
	<body class="is-preload">

		<!-- Wrapper-->
			<div id="wrapper">

				<!-- Nav -->
					<nav id="nav">
						<a href="#Result" class="icon solid fa-folder"><span>General</span></a>
						<!-- <a href="#Advance" class="icon solid fa-folder"><span>Advanced</span></a>
						<a href="#Filter" class="icon solid fa-folder"><span>Filter</span></a> -->
					</nav>

				<!-- Main -->
					<div id="main">

						<!-- General_search -->
							<article id="Result" class="panel">
								<header>
									<h2 align="center">Search Results</h2>
								</header>
								<div align="center">
									<p>
										You entered:
									</p>
									<p>
										<?php
										$query1  = "";
										$query1 = !empty($_POST['general_query']) ? $_POST['general_query'] : "";
										echo $query1;
										?>
								</p>

							</article>

							<div class="row">

								<!-- Default Card Example -->
	              <div class="card mb-4">
	                <div class="card-header">
	                  <h6 class="m-0 font-weight-bold text-primary">Sources</h6>
	                </div>
	                <div class="card-body">
										Publication Name: e.g. New York Times<br>
										<?php
										$query = "";
										$query = !empty($_POST['general_query']) ? $_POST['general_query'] : '';
										echo $query;
										?>
									</div>
	              </div>

								<!-- Basic Card Example -->
	              <div class="card shadow mb-4">
	                <div class="card-header py-3">
	                  <h6 class="m-0 font-weight-bold text-primary">Search history</h6>
	                </div>
	                <div class="card-body">
										Last organization searched: e.g. Samsumg<br>
										<?php
										$query = "";
										$query = !empty($_POST['general_query']) ? $_POST['general_query'] : '';
										echo $query;
										?>
	                </div>
	              </div>

	            </div>

							<div class="card shadow mb-4">
								<div class="card-header py-3">
									<h6 class="m-0 font-weight-bold text-primary">Relations</h6>
								</div>
								<div class="card-body">
									Relations extracted from the RE model: e.g. 1, 2, 3 where the digits indicate a certain relation.<br>
									<?php
									$query = "";
									$query = !empty($_POST['general_query']) ? $_POST['general_query'] : '';
									echo $query;
									?>
								</div>
							</div>

							<div class="card shadow mb-4">
								<div class="card-header py-3">
									<h6 class="m-0 font-weight-bold text-primary">Lexical Dispersion Plot</h6>
								</div>
								<div class="card-body">
									The plot shows how often and which positions certain words appear in a text corpus.<br>
									<img src="plot.jpg" alt="Lexical Dispersion Plot" width="500" height="333">
									<br>
									<?php
									$query = "";
									$query = !empty($_POST['general_query']) ? $_POST['general_query'] : '';
									echo $query;
									?>
								</div>
							</div>

							<div class="row">

		            <!-- Earnings (Monthly) Card Example -->
		            <div class="col-xl-3 col-md-6 mb-4">
		              <div class="card border-left-primary shadow h-100 py-2">
		                <div class="card-body">
		                  <div class="row no-gutters align-items-center">
		                    <div class="col mr-2">
		                      <div class="text-xs font-weight-bold text-primary text-uppercase mb-1">Industry</div>
		                      <div class="h5 mb-0 font-weight-bold text-gray-800">Computer hardware</div>
		                    </div>
		                  </div>
		                </div>
		              </div>
		            </div>

		            <!-- Earnings (Monthly) Card Example -->
		            <div class="col-xl-3 col-md-6 mb-4">
		              <div class="card border-left-success shadow h-100 py-2">
		                <div class="card-body">
		                  <div class="row no-gutters align-items-center">
		                    <div class="col mr-2">
		                      <div class="text-xs font-weight-bold text-success text-uppercase mb-1">Headquaters</div>
		                      <div class="h5 mb-0 font-weight-bold text-gray-800">1 Apple Park Way
Cupertino, California, United States</div>
		                    </div>
		                  </div>
		                </div>
		              </div>
		            </div>

		            <!-- Earnings (Monthly) Card Example -->
		            <div class="col-xl-3 col-md-6 mb-4">
		              <div class="card border-left-info shadow h-100 py-2">
		                <div class="card-body">
		                  <div class="row no-gutters align-items-center">
		                    <div class="col mr-2">
		                      <div class="text-xs font-weight-bold text-info text-uppercase mb-1">Products</div>
													<div class="h5 mb-0 mr-3 font-weight-bold text-gray-800">Macintoch</div>
		                    </div>
		                  </div>
		                </div>
		              </div>
		            </div>

		            <!-- Pending Requests Card Example -->
		            <div class="col-xl-3 col-md-6 mb-4">
		              <div class="card border-left-warning shadow h-100 py-2">
		                <div class="card-body">
		                  <div class="row no-gutters align-items-center">
		                    <div class="col mr-2">
		                      <div class="text-xs font-weight-bold text-warning text-uppercase mb-1">Website</div>
		                      <div class="h5 mb-0 font-weight-bold text-gray-800">www.apple.com</div>
		                    </div>
		                  </div>
		                </div>
		              </div>
		            </div>
		          </div>

							<!-- Begin Page Content -->
							<div class="container-fluid">

								<!-- Content Row -->
								<div class="row">

									<!-- Donut Chart -->
									<div class="col-xl-4 col-lg-5">
										<div class="card shadow mb-4">
											<!-- Card Header - Dropdown -->
											<div class="card-header py-3">
												<h6 class="m-0 font-weight-bold text-primary">Donut Chart</h6>
											</div>
											<!-- Card Body -->
											<div class="card-body">
												<div class="chart-pie pt-4">
													<canvas id="trychart"></canvas>
												</div>
												<div class="mt-4 text-center small">
													<span class="mr-2">
														<i class="fas fa-circle text-primary"></i> Operating Expences (1)
													</span>
													<span class="mr-2">
														<i class="fas fa-circle text-success"></i> Net Income (2)
													</span>
													<span class="mr-2">
														<i class="fas fa-circle text-info"></i> Non-operating Expences (3)
													</span>
													<br>
													<br>
													Operating Income (4) = (2) + (3)<br>
													Revenue = (4) + (1)<br>
													Revenue = (1) + (2) + (3)
												</div>
										</div>
									</div>
								</div>

								<!-- Project Card Example -->
								<div class="card shadow mb-4">
									<div class="card-header py-3">
										<h6 class="m-0 font-weight-bold text-primary">Projects</h6>
									</div>
									<div class="card-body">
										Apple Inc. is an American multinational technology company headquartered in Cupertino, California, that designs, develops, and sells consumer electronics, computer software, and online services. It is considered one of the Big Five technology companies, alongside Microsoft, Amazon, Google, and Facebook.[6][7][8]

										The company's hardware products include the iPhone smartphone, the iPad tablet computer, the Mac personal computer, the iPod portable media player, the Apple Watch smartwatch, the Apple TV digital media player, the AirPods wireless earbuds and the HomePod smart speaker. Apple's software includes macOS, iOS, iPadOS, watchOS, and tvOS operating systems, the iTunes media player, the Safari web browser, the Shazam acoustic fingerprint utility, and the iLife and iWork creativity and productivity suites, as well as professional applications like Final Cut Pro, Logic Pro, and Xcode. Its online services include the iTunes Store, the iOS App Store, Mac App Store, Apple Music, Apple TV+, iMessage, and iCloud. Other services include Apple Store, Genius Bar, AppleCare, Apple Pay, Apple Pay Cash, and Apple Card.
									</div>
								</div>

							</div>
							<!-- /.container-fluid -->




					</div>


							<div class="card shadow mb-4">
		            <div class="card-header py-3">
		              <h6 class="m-0 font-weight-bold text-primary">Facts</h6>
		            </div>
		            <div class="card-body">
		              <div class="table-responsive">
		                <table class="table table-bordered" id="dataTable" width="100%" cellspacing="0">
		                  <thead>
		                    <tr>
		                      <th>A</th>
		                      <th>B</th>
		                      <th>C</th>
		                      <th>D</th>
		                      <th>E</th>
		                      <th>F</th>
		                    </tr>
		                  </thead>
		                  <tfoot>
		                    <tr>
		                      <th>A</th>
		                      <th>B</th>
		                      <th>C</th>
		                      <th>D</th>
		                      <th>E</th>
		                      <th>F</th>
		                    </tr>
		                  </tfoot>
		                  <tbody>
		                    <tr>
		                      <td>x</td>
		                      <td>x</td>
		                      <td>x</td>
		                      <td>x</td>
		                      <td>x</td>
		                      <td>x</td>
		                    </tr>
		                    <tr>
		                      <td>x</td>
		                      <td>x</td>
		                      <td>x</td>
		                      <td>x</td>
		                      <td>x</td>
		                      <td>x</td>
		                    </tr>
		                    <tr>
		                      <td>x</td>
		                      <td>x</td>
		                      <td>x</td>
		                      <td>x</td>
		                      <td>x</td>
		                      <td>x</td>
		                    </tr>
		                    <tr>
		                      <td>x</td>
		                      <td>x</td>
		                      <td>x</td>
		                      <td>x</td>
		                      <td>x</td>
		                      <td>x</td>
		                    </tr>
		                  </tbody>
		                </table>
		              </div>
		            </div>
		          </div>

							<a href="general.html" style="text-align: center;" class="btn btn-primary btn-icon-split">
								<span class="icon text-white-50">
									<i class="fas fa-flag"></i>
								</span>
								<span class="text">Split Button Primary</span>
							</a>



			</div>

		<!-- Scripts -->
			<script src="assets/js/jquery.min.js"></script>
			<script src="assets/js/browser.min.js"></script>
			<script src="assets/js/breakpoints.min.js"></script>
			<script src="assets/js/util.js"></script>
			<script src="assets/js/main.js"></script>


			<!-- Bootstrap core JavaScript-->
			<script src="vendor/jquery/jquery.min.js"></script>
			<script src="vendor/bootstrap/js/bootstrap.bundle.min.js"></script>

			<!-- Core plugin JavaScript-->
			<script src="vendor/jquery-easing/jquery.easing.min.js"></script>

			<!-- Custom scripts for all pages-->
			<script src="js/sb-admin-2.min.js"></script>

			<!-- Page level plugins -->
			<script src="vendor/chart.js/Chart.min.js"></script>
			<script src="vendor/datatables/jquery.dataTables.min.js"></script>
		  <script src="vendor/datatables/dataTables.bootstrap4.min.js"></script>

			<!-- Page level custom scripts -->
			<script src="js/demo/chart-area-demo.js"></script>
			<script src="js/demo/chart-pie-demo.js"></script>
			<script src="js/demo/chart-bar-demo.js"></script>
			<script src="js/demo/datatables-demo.js"></script>

			<script>
			Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
			Chart.defaults.global.defaultFontColor = '#858796';
			var ctx = document.getElementById("trychart");
			var trychart = new Chart(ctx, {
				type: 'doughnut',
				data: {
					labels: ["Net Income", "Non-operating Expences", "Operating Expences"],
					datasets: [{
						data: [55, 30, 15],
						backgroundColor: ['#4e73df', '#1cc88a', '#36b9cc'],
						hoverBackgroundColor: ['#2e59d9', '#17a673', '#2c9faf'],
						hoverBorderColor: "rgba(234, 236, 244, 1)",
					}],
				},
				options: {
					maintainAspectRatio: false,
					tooltips: {
						backgroundColor: "rgb(255,255,255)",
						bodyFontColor: "#858796",
						borderColor: '#dddfeb',
						borderWidth: 1,
						xPadding: 15,
						yPadding: 15,
						displayColors: false,
						caretPadding: 10,
					},
					legend: {
						display: false
					},
					cutoutPercentage: 80,
				},
			});

			</script>

	</body>
</html>
