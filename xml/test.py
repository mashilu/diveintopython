from xml.dom import minidom

xmldoc = minidom.parse("E:\\1_CODE\\0_github\\python\\diveintopython\\xml\\kant.xml")

print(xmldoc.toxml())