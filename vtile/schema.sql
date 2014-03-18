drop table if exists tiles;
create table tiles (
id integer primary key autoincrement,
content text not null,
tile_row integer not null,
tile_column integer not null,
zoom integer not null
);
create index tindex on tiles(zoom,tile_row,tile_column);
