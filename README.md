pachyderm
===
Pachyderm is a simple Python script that processes Evernote export files and removes notes based upon their tagging.

##Installation
You can install pachyderm using pip.

    $ pip install -r requirements.txt

##Usage
Pachyderm requires that you specify the following arguments:

* export_file - The path to read the export file to process
* output_file - The path to write the post-processed export file
* tag - Notes tagged with this tag will not be included in the post-processed export file


    $ python pachyderm <export file> <output file> <tag>
