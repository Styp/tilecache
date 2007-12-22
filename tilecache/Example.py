#!/usr/bin/python

from TileCache.Service import Service, modPythonHandler, cgiHandler
from TileCache.Cache import DiskCache
import TileCache.Layers.WMS as WMS
import TileCache.Layers.MapServer as MS

myService = Service (
  DiskCache("/www/wms-c/cache"), 
  { 
    "basic"     : MS.MapServer( "basic", "/www/wms-c/basic.map" ),
    "satellite" : MS.MapServer( "satellite", "/www/wms-c/basic.map",
                                extension = "jpeg" ),
    "cascade"   : WMS.WMS( "basic", "http://labs.metacarta.com/wms/vmap0?",
                                extension = "jpeg" ),
    "DRG"       : WMS.WMS( "DRG", "http://terraservice.net/ogcmap.ashx?",
                                extension = "jpeg"  ),
    "OSM"       : WMS.WMS( "roads", 
                    "http://aesis.metacarta.com/cgi-bin/mapserv?FORMAT=png8&" +
                    "map=/home/crschmidt/osm.map&TRANSPARENT=TRUE&",
                    extension = "png"  ),
    "Boston"    : WMS.WMS( 
                    "border,water,openspace,roads,buildings,rapid_transit",
                    "http://nyc.freemap.in/cgi-bin/mapserv?" + 
                    "map=/www/freemap.in/boston/map/gmaps.map&" ),
    "hfoot"     : WMS.WMS( "hfoot", 
                    "http://beta.sedac.ciesin.columbia.edu/mapserver/wms/hfoot?",
                    levels = 20, extension = "jpeg")
  }
) 

def handler (req):
    return modPythonHandler(req, myService)

if __name__ == '__main__':
    cgiHandler(myService)