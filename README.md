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
* mapcss-parser

TWMS is not available via PIP and must be installed manually (at least in Ubuntu this can be done using system package manager, sudo apt-get install python-twms).
Then, install PIP-based packages (sudo pip install -r requirements.txt).
The next step is to install mapcss-parser:
git clone https://github.com/Miroff/mapcss-parser.git
cd mapcss-parser
sudo python setup.py install

For vector tile rendering, a local [osm2pgsql](http://wiki.openstreetmap.org/wiki/Osm2pgsql) database is needed. The default osm2pgsql setup is sufficient.
Alternatively, set the PostgreSQL connection string to __none__ and download an [example set of tiles](http://not-uploaded-yet) covering the area of Cracow, Poland.
The tile set should be placed in "vtile" directory.

KothicJS uses HTML5 Canvas, so a modern web browser is a must. Chrome/Chromium is recommended to get the best performance. Firefox is slower and less stable (can crash during rendering).

Acknowledgements
----------------

The project uses the great [KothicJS](https://github.com/kothic/kothic-js) library by Darafei Praliaskouski ([@Komzpa](https://github.com/Komzpa)), Vladimir Agafonkin ([@mourner](https://github.com/mourner) and Maksim Gurtovenko ([@Miroff](https://github.com/Miroff))
Slightly modified versions of original json_getter and mapcss_converter scripts are included (in "modules" directory), as well as osmosnimki-maps.mapcss style (for SQL hints in vector tile renderer) and icon library from [kothic-js-mapcss](https://github.com/kothic/kothic-js-mapcss) repository.

License
-------

The project is licensed under a two-clause BSD license like its core components.
 
