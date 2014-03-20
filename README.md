MapFiddle
=========


This project aims to be an rapid design tool for custom [OpenStreetMap](http://openstreetmap.org) styles. It's based on [KothicJS](https://github.com/kothic/kothic-js) in-browser map renderer.

Requirements & Installation
---------------------------

The backend is written in Python, and depends on following Python modules:
* Flask
* PIL
* psycopg2
* twms
* cairo
* rsvg
* mapcss-parser

TWMS, cairo and rsvg are not available via PIP and must be installed manually.
In Ubuntu this can be done using system package manager:  
  sudo apt-get install python-twms python-cairo python-rsvg  
Then, install PIP-based packages:  
  sudo pip install -r requirements.txt  
The final step is to install mapcss-parser:  
git clone https://github.com/Miroff/mapcss-parser.git  
cd mapcss-parser  
sudo python setup.py install  

After that, the app can be run using Flask development server:

  python app.py

Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in a web browser to verify.

For production deployments, follow the instructions for [deploying Flask apps](http://flask.pocoo.org/docs/deploying/#deployment).

For vector tile rendering, a local [osm2pgsql](http://wiki.openstreetmap.org/wiki/Osm2pgsql) database is needed. The default osm2pgsql setup is sufficient.
Alternatively, set the PostgreSQL connection string to __none__ and download an [example set of tiles](https://www.dropbox.com/s/jrk08zxbnukaa57/vtile.db) covering the area of Cracow, Poland.
The tile set should be placed in "vtile" directory.

Demo page
---------

You can test MapFiddle on the demo page: [mapfiddle.pl](http://mapfiddle.pl)
Please note that this is hosted on Amazon EC2 Micro instance for now, so the performance can be horrible.

Limitations
-----------

The tool is still rough around the edges. You can't download the icons (neither CSS sprite nor single PNG images), or store your style on the server.
Also, the vector tile rendering script is VERY slow. 
 
KothicJS uses HTML5 Canvas, so a modern web browser is a must. Chrome/Chromium is recommended to get the best performance. Firefox is slower and less stable (can crash during rendering).

Acknowledgements
----------------

The project uses the great [KothicJS](https://github.com/kothic/kothic-js) library by Darafei Praliaskouski ([@Komzpa](https://github.com/Komzpa)), Vladimir Agafonkin ([@mourner](https://github.com/mourner) and Maksim Gurtovenko ([@Miroff](https://github.com/Miroff))
Slightly modified versions of original json_getter and mapcss_converter scripts are included (in "modules" directory), as well as osmosnimki-maps.mapcss style (for SQL hints in vector tile renderer) and icon library from [kothic-js-mapcss](https://github.com/kothic/kothic-js-mapcss) repository.

License
-------

The project is licensed under a two-clause BSD license like its core components.
 
