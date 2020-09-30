#fix bug
exec { 'update':
  path    => '/bin',
  command => "sed -i -e 's/phpp/php/g' /var/www/html/wp-settings.php",
}
