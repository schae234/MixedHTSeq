MixedHTSeq
----------
By default, HTSeq has a count script for doing either paired ends or single end reads.
MixedHTSeq extends this to cover cases where you have a mixture of the two due to 
QC tools like [AdapterRemoval](http://www.ncbi.nlm.nih.gov/pubmed/22748135). 

Installation
------------
MixedHTSeq can be installed using the following commands (on linux machines)
```
git clone https://github.com/schae234/MixedHTSeq.git
cd MixedHTSeq
pip install numpy pandas 
python setup.py install
```

**Note**: MixedHTSeq requires python2.7 and numpy

Usage
-----
MixedHTSeq comes with several scripts which are in the `scripts/` directory.

```
cd scripts/
python mixed_count.py --help
```

References
----------
See original Docs [here](http://www-huber.embl.de/users/anders/HTSeq/doc/overview.html)

License
-------
MixedHTSeq and HTSeq are free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

The full text of the GNU General Public License, version 3, can be found here: http://www.gnu.org/licenses/gpl-3.0-standalone.html
