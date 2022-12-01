
from email.policy import default
from click import style
import folium
import pandas

waterfalls = pandas.read_csv("IranWaterfalls.txt", sep=",",encoding='ISO-8859-1')




def display_color(point):
    if waterfalls["Height/Meter"][point] < 20:
        color = "lightgreen"
    elif 20 <= waterfalls["Height/Meter"][point] <=50:  
        color ="orange"
    else :
        color = "red"
    return color


def world_map_borders(map):

    world_map_borders = open('world.json',encoding="utf-8-sig").read()
    style= {"fillColor":'#00000000'}
    folium.GeoJson(data=world_map_borders, style_function=lambda x: style).add_to(map)
    # folium.TileLayer('https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png',attr='opentop').add_to(map)
    # folium.TileLayer('https://{s}.tile.openstreetmap.de/tiles/osmde/{z}/{x}/{y}.png',attr='openstreet').add_to(map)
    folium.LayerControl().add_to(map)




def display_setings():
    lat_long = waterfalls[["Longitude","Latitude"]]
    lat_long_list = lat_long.values.tolist()
    map = folium.Map(location=[32.4279,53.6880], zoom_start=6,tiles='stamenterrain', attr='geomap',default=True)
    
    world_map_borders(map)
    for point in range(0 , len(lat_long_list)):
        city_name =waterfalls["City"][point]
        waterfall_name = waterfalls["Name"][point]
        waterfall_height = waterfalls["Height/Meter"][point]
        popup_text = f"""<body>
                            <b>Waterfall</b><br/><hr/>
                            City:<br/><strong>{city_name}</strong><br/><hr><br/>
                            Name: <strong>{waterfall_name}</strong><hr/><br/>
                            Height:<strong> {waterfall_height} Meters</strong>
                        </body>
                        """

        
        
        display_frame = folium.IFrame(html = popup_text, width=150, height=250)
        folium.Marker(lat_long_list[point], popup=folium.Popup(display_frame),icon = folium.Icon(color=display_color(point), icon_color="blue", icon='tint')).add_to(map)
        map.save('waterfalls.html')

  


def final_call():
    display_setings()

final_call()
    
