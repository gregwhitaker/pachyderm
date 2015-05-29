from lxml import etree
import sys

def usage():
    print "usage: pachyderm <input-file> <output-file> <tag>"

if __name__ == '__main__':
    # Checking for input and output file parameters
    if sys.argv.__len__() < 4:
        usage()
        sys.exit(1)

    inputFile = sys.argv[1]
    outputFile = sys.argv[2]
    tag = sys.argv[3]

    print "Processing Evernote Export File: " + inputFile

    # Parsing the input file
    parser = etree.XMLParser(strip_cdata=False)
    doc = etree.parse(inputFile, parser)

    totalCnt = 0
    includedCnt = 0
    excludedCnt = 0

    # Iterate over all "note" elements in the document
    for element in doc.iter("note"):
        exclude = False
        # Iterate over all "tag" elements within the "note" element
        for tagElement in element.iter("tag"):
            if tagElement.text == tag:
                excludedCnt += 1
                element.getparent().remove(element)
                exclude = True
                break

        if not exclude:
            includedCnt += 1

        totalCnt += 1

    # Write new document
    doc.write(outputFile, encoding="UTF-8", xml_declaration=True)

    print "Exported Notes: " + str(includedCnt)
    print "Excluded Notes: " + str(excludedCnt)
    print "Total Notes: " + str(totalCnt)