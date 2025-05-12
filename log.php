<?php
echo "<!DOCTYPE html><html><head>
<title>Visualisation des logs</title>
<meta charset='utf-8'>
<style>
body { font-family: Arial, sans-serif; background: #f4f4f4; margin: 0; padding: 0; }
.container { max-width: 800px; margin: 40px auto; background: #fff; border-radius: 8px; box-shadow: 0 2px 8px #aaa; padding: 30px; }
.log-entry { background: #222; color: #0f0; padding: 10px 15px; border-radius: 5px; margin-bottom: 8px; font-size: 1em; font-family: 'Consolas', monospace; }
h2 { color: #333; }
button { margin-top: 20px; padding: 10px 20px; border: none; background: #333; color: #fff; border-radius: 5px; cursor: pointer; }
button:hover { background: #0f0; color: #222; }
</style>
</head><body>
<div class='container'>
<h2>Logs reçus :</h2>";

if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['log'])) {
    $log = $_POST['log'];
    file_put_contents("reception.log", $log, FILE_APPEND);
    echo "<p>Log reçu !</p>";
} else {
    if (file_exists("reception.log")) {
        $lines = file("reception.log");
        if (count($lines) > 0) {
            foreach ($lines as $line) {
                echo "<div class='log-entry'>" . htmlspecialchars($line) . "</div>";
            }
        } else {
            echo "<p>Aucun log reçu pour le moment.</p>";
        }
        echo "<form method='post'><button type='submit' name='clear'>Vider les logs</button></form>";
        if (isset($_POST['clear'])) {
            file_put_contents("reception.log", "");
            header("Refresh:0");
        }
    } else {
        echo "<p>Aucun log recu pour le moment.</p>";
    }
}

echo "</div></body></html>";
?>