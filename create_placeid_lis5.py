import json
import requests
import time

f = open("/Users/hoecheeyam/Desktop/google_maps/Willoughby_results/Hardware.txt",'w')

x = [151.1457606,151.1510095,151.1667565,151.1772544,151.1772544,151.1772544,151.1825034,151.1825034,151.1825034,151.1825034,151.1825034,151.1825034,151.1877524,151.1877524,151.1877524,151.1877524,151.1877524,151.1930014,151.1930014,151.1930014,151.1930014,151.1930014,151.1930014,151.1982504,151.1982504,151.1982504,151.1982504,151.1982504,151.1982504,151.2034993,151.2034993,151.2034993,151.2087483,151.2087483,151.2139973,151.2139973,151.2139973,151.2192463]
y =[-33.8030305,-33.806061,-33.7969695,-33.8151525,-33.8030305,-33.7969695,-33.818183,-33.812122,-33.806061,-33.8,-33.793939,-33.787878,-33.8212135,-33.8151525,-33.8090915,-33.7969695,-33.7909085,-33.824244,-33.818183,-33.812122,-33.793939,-33.787878,-33.781817,-33.8212135,-33.8090915,-33.8030305,-33.7969695,-33.7909085,-33.7848475,-33.818183,-33.787878,-33.781817,-33.8090915,-33.7969695,-33.812122,-33.8,-33.787878,-33.8151525]

# x =[151.1457606]
# y =[-33.8030305]

c=0
for cord in x:
		url_radar="https://maps.googleapis.com/maps/api/place/radarsearch/json?location="+str(y[c])+","+str(x[c])+"&radius=350&keyword=Hardware_stores&key=AIzaSyCP0IsHcWtO1DZomj02raI1rJw6-mm3exI"
		r_radar=requests.get(url_radar)
		r_radar_json=r_radar.json()
		json_object_counter=0
		for i in r_radar_json["results"]:
			place_ids=r_radar_json["results"][json_object_counter]["place_id"]
			url="https://maps.googleapis.com/maps/api/place/details/json?placeid="+place_ids+"&key=AIzaSyCP0IsHcWtO1DZomj02raI1rJw6-mm3exI"
			r=requests.get(url)
			this_place=r.json()
			# print(this_place["status"])
			if this_place["status"] == "OVER_QUERY_LIMIT":
				time.sleep(2)
				continue
			name=this_place["result"].setdefault("name",None)
			lat=this_place["result"]["geometry"]["location"].setdefault("lat",None)
			longt=this_place["result"]["geometry"]["location"].setdefault("lng",None)
			types=this_place["result"].setdefault("types",None)
			format_add=this_place["result"].setdefault("formatted_address",None)
			f.write(str(c)+"+"+str(name)+"+"+str(lat)+"+"+str(longt)+"+"+format_add+"+"+str(types)+"\n")
			print(json_object_counter)
			json_object_counter=json_object_counter+1
		c=c+1
f.close()
