pachyderm
===
Pachyderm is a simple Python script that processes Evernote export files and removes notes based upon their tagging.

##Installation
You can install pachyderm using pip.

    $ pip install -r requirements.txt

##Usage

    $ python pachyderm <input_file> <output_file> <tag>
    
Pachyderm requires that you specify the following arguments:

* input_file - The path to read the input Evernote ENEX file to process
* output_file - The path to write the post-processed Evernote ENEX output file
* tag - Notes tagged with this tag will not be included in the output file

###Example
The following command will load notes from the *sample.enex* file, remove any notes tagged "*private*", and write the remaining notes to the *output.enex* file.

    $ python pachyderm ./sample/sample.enex ./sample/output.enex private
