#!/usr/bin/python

_BUGSENDER = "diffpy@diffpy.org"
_BUGEMAIL = "diffpy-dev@googlegroups.com"
_SMTP_SERVER = "localhost"

_MSG = """\
From: %(bugsender)s
Subject: [%(component)s bug] %(summary)s
To: %(bugemail)s

reporter: %(reporter)s

summary: %(summary)s 

description: %(description)s 

component: %(component)s

version: %(version)s

traceback: %(traceback)s
"""

def email(req, **kwargs):
    """Process bugreport form and submit it to _BUGEMAIL address.
    """
    # process form arguments
    flds = {
        # hidden data entries
        'bugemail' : _BUGEMAIL,
        'bugsender' : _BUGSENDER,
        # entries from the form
        'reporter' : 'anonymous',
        'summary' : '',
        'description' : '',
        'component' : '',
        'version' : '',
        'traceback' : ''
    }
    flds.update(kwargs)
    # check required fields
    required_fields = ('summary', 'description')
    missing_fields = [f for f in required_fields if not flds.get(f)]
    if missing_fields:
        emsg = "\n".join([
            "Required fields(s) missing: %s." % ", ".join(missing_fields),
            "Please go back and correct the error"
            ]) + "\n"
        return emsg
    # build email message
    msg = _MSG % flds
    # send it out
    import smtplib
    conn = smtplib.SMTP(_SMTP_SERVER)
    conn.sendmail(flds['bugsender'], [flds['bugemail']], msg)
    conn.quit()
    # show message that was sent:
    out = "\n".join([
            "<html>",
            "<p>Bugreport emailed to %s" % flds['bugemail'],
            "</p>",
            "<pre>" + msg + "</pre></html>"
            ]) + "\n"
    return out

# End of file
