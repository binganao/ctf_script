<?php
if (!isset($argv[1])) {
  echo("usage: php base64.php \"raw text\"");
}
else {
  $raw = $argv[1];
  echo(base64_encode($raw));
  echo "\n\n";
  echo(base64_decode($raw));
}
echo("\n");
?>