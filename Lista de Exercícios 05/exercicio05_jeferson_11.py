arquivo = open('ola.html', 'w', encoding='utf-8')
arquivo.write('''<!DOCTYPE html>
<html lang='pt-br'>
    <head>
        <meta charset="utf-8" />
        <title>Exemplo</title>
    </head>
    <body>
        <p>Olá, mundo!</p>
    </body>
</html>''')
arquivo.close()
