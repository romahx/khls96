<body lang="ru-RU" link="#000080" vlink="#800000" dir="ltr"><p align="center" style="line-height: 100%; margin-bottom: 0cm">
<font face="Liberation Serif, serif"><font size="4" style="font-size: 14pt">Необходимые действия для установки application (ОС Ubuntu)</font></font></p>
<ol>
	<li><p align="left" style="line-height: 100%; margin-bottom: 0cm"><font face="Liberation Serif, serif"><font size="4" style="font-size: 14pt">Скачать
	и установить последнюю версию Python(актуальная версия на 20.04.22 — 3.10.6.1):</font></font></p>
	<pre class="western" style="text-align: left"><code class="western"><font face="Liberation Serif, serif"><font size="4" style="font-size: 14pt"><span style="font-weight: normal">sudo apt install python3</span></font></font></code></pre>
	<li><p align="left" style="line-height: 100%; margin-bottom: 0cm"><font face="Liberation Serif, serif"><font size="4" style="font-size:14pt">Установить последнюю версию PostgreSQL:</font></font></p>
	<pre class="western" style="text-align: left"><code class="western"><font face="Liberation Serif, serif"><font size="4" style="font-size: 14pt"><span style="font-weight: normal">sudo apt-get install postgresql postgresql-contrib</span></font></font></code></pre>
	<li><p align="left" style="line-height: 100%; margin-bottom: 0cm"><font face="Liberation Serif, serif"><font size="4" style="font-size: 14pt">Клонировать репозиторий в нужный каталог командой(в Терминале):</font></font></p>
	<pre class="western" style="text-align: left"><code class="western"><font face="Liberation Serif, serif"><font size="4" style="font-size: 14pt"><span style="font-weight: normal">git clone https://github.com/romahx/khls96.git</span></font></font></code></pre>
	<li><p align="left" style="line-height: 100%; margin-bottom: 0cm"><font face="Liberation Serif, serif"><font size="4" style="font-size: 14pt">Перейти
	в каталог:</font></font></p>
	<pre class="western" style="text-align: left"><code class="western"><font face="Liberation Serif, serif"><font size="4" style="font-size: 14pt"><span style="font-weight: normal">cd khls96</span></font></font></code></pre>
	<li><p align="left" style="line-height: 100%; margin-bottom: 0cm"><font face="Liberation Serif, serif"><font size="4" style="font-size: 14pt">Установить виртуальное окружение:</font></font></p>
	<<pre class="western" style="text-align: left"><code class="western"><font face="Liberation Serif, serif"><font size="4" style="font-size: 14pt"><span style="font-weight: normal">virtualenv env</span></font></font></code></pre>
	<li><p align="left" style="line-height: 100%; margin-bottom: 0cm"><font face="Liberation Serif, serif"><font size="4" style="font-size: 14pt">Активировать виртуальную среду:</font></font></p>
	<pre class="western" style="text-align: left"><code class="western"><font face="Liberation Serif, serif"><font size="4" style="font-size: 14pt"><span style="font-weight: normal">source env/bin/activate</span></font></font></code></pre>
	<li><p align="left" style="line-height: 100%; margin-bottom: 0cm"><font face="Liberation Serif, serif"><font size="4" style="font-size: 14pt">В	виртуальном окружении установить зависимости с помощью pip:</font></font></p>
	<pre class="western" style="text-align: left"><code class="western"><font face="Liberation Serif, serif"><font size="4" style="font-size: 14pt"><span style="font-weight: normal">pip install -r requirements.txt</span></font></font></code></pre>
	<p align="left" style="line-height: 100%; margin-bottom: 0cm"><font face="Liberation Serif, serif"><font size="4" style="font-size: 14pt">При
	необходимости обновить pip.</font></font></p>
	<li><p align="left" style="line-height: 100%; margin-bottom: 0cm"><font face="Liberation Serif, serif"><font size="4" style="font-size: 14pt">В
	файле config.py настраиваем доступ к существующей базе данных:</font></font></p>
	<pre class="western" style="text-align: left"><code class="western"><font face="Liberation Serif, serif"><font size="4" style="font-size: 14pt"><span style="font-weight: normal">SQLALCHEMY_DATABASE_URI = 'postgresql://root:pass@host:port/my_db', где:</span></font></font></code></pre>
	<p align="left" style="line-height: 100%; margin-bottom: 0cm"><font face="Liberation Serif, serif"><font size="4" style="font-size: 14pt">-
	root — имя пользователя;</font></font></p>
	<p align="left" style="line-height: 100%; margin-bottom: 0cm"><font face="Liberation Serif, serif"><font size="4" style="font-size: 14pt">-
	pass — пароль;</font></font></p>
	<p align="left" style="line-height: 100%; margin-bottom: 0cm"><font face="Liberation Serif, serif"><font size="4" style="font-size: 14pt">-
	host — местоположение базы данных;</font></font></p>
	<p align="left" style="line-height: 100%; margin-bottom: 0cm"><font face="Liberation Serif, serif"><font size="4" style="font-size: 14pt">-
	port — порт сервера базы данных(стандартное значение)</font></font></p>
	<p align="left" style="line-height: 100%; margin-bottom: 0cm"><font face="Liberation Serif, serif"><font size="4" style="font-size: 14pt">-
	my_db — имя базы данных.</font></font></p>
	<li><p align="left" style="line-height: 100%; margin-bottom: 0cm"><font face="Liberation Serif, serif"><font size="4" style="font-size: 14pt">В
	виртуальном окружении запустить приложение командой:</font></font></p>
	<pre class="western" style="text-align: left"><code class="western"><font face="Liberation Serif, serif"><font size="4" style="font-size: 14pt"><span style="font-weight: normal">python3 app.py</span></font></font></code></pre>
</ol>
