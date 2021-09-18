<?php
if (!isset($argv[1])) {
  echo("usage: php urlcode.php \"raw text\"");
}
else {
  $raw = $argv[1];
  echo(urlencode($raw));
  echo "\n\n";
  echo(urldecode($raw));
}
echo("\n");
?>