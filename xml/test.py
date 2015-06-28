from xml.dom import minidom

xmldoc = minidom.parse("E:\\1_CODE\\0_github\\python\\diveintopython\\xml\\binary.xml")

reflist = xmldoc.getElementsByTagName("ref")

typeRef = reflist[1]

print(typeRef.toxml())