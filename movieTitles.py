#!/usr/bin/python
# Demonstrating SAX-based parsing of XML
import sys
import xml.sax

class XmlReader( xml.sax.ContentHandler ):
  def __init__(self):
    xml.sax.ContentHandler.__init__(self)
    self.titles = []
    self.titleFound = False

  def startElement( self, name, attributes ):
    if name == 'Title':
      self.titleFound = True

  def endElement( self, name ) :
    self.titleFound = False

  def characters( self, content ) :
    # strip only removes spaces!
    content = content.strip()
    if self.titleFound and content: 
        print "title is:", content
        self.titles.append(content)

def main():
  print "Beginning XML processor..."
  if len(sys.argv) != 2:
    print "usaage:", sys.argv[0], "<xml file>"
    sys.exit()
  file = sys.argv[1]
  try:
    xml.sax.parse ( file, XmlReader() )
  except IOError, message:
    print "Error reading file: ", message
  except xml.sax.SAXParseException, message:
    print "Error parsing file: ", message

if __name__ == "__main__":
  main()
