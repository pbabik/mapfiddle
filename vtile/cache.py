class VTileCache:
    def __init__(self):
        import sqlite3
        import os
        self.dbconn = sqlite3.connect(os.path.join(os.path.dirname(__file__),'vtile.db'))
    
    def init_db(self):
        """ Helper method to create and index the required table """
        import os
        f = open(os.path.join(os.path.dirname(__file__),'schema.sql'),'r') #read schema from SQL file
        self.dbconn.cursor().executescript(f.read())
        self.dbconn.commit()
    	
    def get_tile(self,x,y,z):
        """ Get vector tile form cache, based on XYZ coordinates """
        query = "SELECT content FROM tiles WHERE zoom = ? AND tile_row = ? AND tile_column = ?" #try to find a tile 
        try:
            cur = self.dbconn.execute(query,[z,x,y])
        except: #the database is totally empty - create required table first
            self.init_db()
            return None #simulate "not found" response to trigger rendering
        return cur.fetchone()

    def set_tile(self,x,y,z,data): 
        """ Insert new vector tile into cache """
        query = "INSERT INTO tiles(content,tile_row,tile_column,zoom) VALUES(?,?,?,?)"
        self.dbconn.execute(query,[data,x,y,z])
        self.dbconn.commit()
