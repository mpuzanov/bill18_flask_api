# API - сервис по приборам учёта

### Возвращаем список улиц
SITE + '/streets
### Возвращаем список домов по заданной улице
SITE + '/builds/<street_name>
### Возвращаем список помещений по заданному дому
SITE + '/flats/<street_name>/<nom_dom>
### Возвращаем список лицевых в помещении
SITE + '/lics/<street_name>/<nom_dom>/<nom_kvr>
### Возвращаем информацию по заданному лицевому счету
SITE + '/lic/<int:lic>
### Возвращаем список приборов учета по заданному лицевому счету
SITE + '/infoDataCounter/<int:lic>
### Возвращаем список показаний приборов учета по заданному лицевому счету
SITE + '/infoDataCounterValue/<int:lic>'
### Добавление ППУ
SITE + '/puAddValue/<int:pu_id>/<float:value>
### Удаление ППУ
SITE + '/puDelValue/<int:pu_id>/<int:id_value>
