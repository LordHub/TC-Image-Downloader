import urllib.request

resource = urllib.request.urlopen("http://cloud10.todocoleccion.online/comics-usa/tc/2017/01/31/12/74551561_1485860743_rot1485860790.jpg")
output = open("file01.jpg","wb")
output.write(resource.read())
output.close()
