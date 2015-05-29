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

    processedCnt = 0
    excludedCnt = 0

    # Iterate over all "note" tags in the document
    for element in doc.iter("note"):
        personal = False
        for tagElement in element.iter("tag"):
            if tagElement.text == 'personal':
                personal = True
                excludedCnt += 1
                break

        if not personal:
            print element

        processedCnt += 1

    print "Total Notes: " + str(processedCnt)
    print "Excluded Notes: " + str(excludedCnt)
    sys.exit(0)

