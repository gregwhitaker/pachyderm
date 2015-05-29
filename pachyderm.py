from lxml import etree
import sys

def usage():
    print "usage: pachyderm <input-file> <output-file>"

if __name__ == '__main__':
    # Checking for input and output file parameters
    if sys.argv.__len__() < 3:
        usage()
        sys.exit(1)

    print "Processing Evernote Export: " + sys.argv[1]

    # Parsing the export file
    doc = etree.parse(sys.argv[1])

    totalCnt = 0
    includedCnt = 0
    excludedCnt = 0

    # Iterate over all "note" tags in the document
    for element in doc.iter("note"):
        exclude = False
        for tagElement in element.iter("tag"):
            if tagElement.text == 'personal':
                excludedCnt += 1
                element.getparent().remove(element)
                exclude = True
                break

        if not exclude:
            includedCnt += 1

        totalCnt += 1

    print "Exported Notes: " + str(includedCnt)
    print "Excluded Notes: " + str(excludedCnt)
    print "Total Notes: " + str(totalCnt)