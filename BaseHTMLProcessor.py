from sgmllib import SGMLParser

class BaseHTMLProcessor(SGMLParser):
    def reset(self):
        self.pieces = []
        SGMLParser.reset(self)
        
    def unknown_starttag(self, tag, attrs):
        strattrs = "".join([' %s = "%s"' % (key, value) for key, value in attrs])
        self.pieces.append("<%(tag)s%(strattrs)s>" % locals())
        
    def unknown_endtag(self, tag):
        self.pieces.append("</%(tag)s>" % locals())
        
    def handle_charref(self, ref):
        self.pieces.append("&#%(ref)s;" % locals())
        
    def handle_entityref(self, ref):
        self.pieces.append("&%(ref)s" % locals())