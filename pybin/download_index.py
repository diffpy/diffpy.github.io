import os
import re
import time

# Constants

_thisdir = os.path.dirname(os.path.abspath(__file__))
_diffpydir = os.path.dirname(_thisdir)
_statsfile = os.path.join(_diffpydir, 'stats.txt')


def _getDownloadList(drel):
    """Obtain data needed for creating download table for a directory.

    drel    -- directory path relative to _diffpydir

    Return dictionary with items
    ('mtime', 'name', 'dcount', 'fmtsize', 'size', 'fmtmtime')
    """
    downloaddir = os.path.join(_diffpydir, drel)
    ignore = re.compile(r'^[.]|stats.txt')
    lst = []
    for f in os.listdir(downloaddir):
	relpath = os.path.join(drel, f)
	fullpath = os.path.join(downloaddir, f)
	if not os.path.isfile(fullpath) or ignore.match(f): continue
	lst.append({
		'name' : f,
		'relpath' : relpath,
		'fullpath' : fullpath,
		'mtime' : os.path.getmtime(fullpath),
		'size' : os.path.getsize(fullpath),
	})
    # reverse sort by mtime then by name
    lsort = [(-d['mtime'], d['name'], d) for d in lst]
    lsort.sort()
    lst = [ tpl[-1] for tpl in lsort ]
    # add the dcount field
    dcount = {}
    if os.path.isfile(_statsfile):
        for line in open(_statsfile):
            w = line.lstrip('/').split()
            if len(w) != 2:     continue
            dcount[w[0]] = int(w[1])
    for d in lst:
        d['dcount'] = dcount.get(d['relpath'], 0)
    # add fmtsize and fmtmtime fields
    from pathutils import formatbytes
    for d in lst:
        d['fmtsize'] = formatbytes(d['size'],
                bytename='', kiloname='K', meganame='M')
        d['fmtmtime'] = time.strftime('%Y-%m-%d %H:%M',
                time.localtime(d['mtime']) )
    return lst


def _getNameWidth(lst):
    width = max([len(d['name']) for d in lst] + [0])
    width = 4 * (width/4 + 1)
    return width


def _getDownloadHTMLCode(drel):
    lst = _getDownloadList(drel)
    nw = _getNameWidth(lst)
    fmt = "%-@NWs%-20s%-8s%s".replace('@NW', str(nw))
    header = ("<pre>" + fmt + '<hr>') % \
            ('Name', 'Date', 'Size', 'Downloads')
    bodylines = []
    for d in lst:
        anchor = '<a href="%(relpath)s">%(name)s</a>' % d
        anchor += (nw - len(d['name'])) * " "
        bline = fmt % (anchor, d['fmtmtime'], d['fmtsize'], d['dcount'])
        bodylines.append(bline)
    footer = '<hr></pre>'
    code = header + "\n".join(bodylines) + footer
    return code


# Published items

def index(req):
    return download(req)

def download(req):
    return _getDownloadHTMLCode('download')

def packages(req):
    return _getDownloadHTMLCode('packages')


#   <pre>Name                    Last modified      Size  Description<hr><a href="diffpy-1.0b.1232.tgz">diffpy-1.0b.1232.tgz</a>    14-May-2007 21:00  6.9M  
#   <a href="diffpy-1.0b.1232.exe">diffpy-1.0b.1232.exe</a>    14-May-2007 21:00   20M  
#   <a href="diffpy-1.0b.1218.tgz">diffpy-1.0b.1218.tgz</a>    07-May-2007 11:00  7.3M  
#   <a href="diffpy-1.0b.1218.exe">diffpy-1.0b.1218.exe</a>    07-May-2007 11:00   20M  
#   <hr></pre>
