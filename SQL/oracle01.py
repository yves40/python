#-----------------------------------------------------------------------------------------------------------
#   oracle01.py
#
#   Nov 11 2016     Initial
#-----------------------------------------------------------------------------------------------------------

import cx_Oracle

import os 

os.environ["NLS_LANG"] = ".AL32UTF8" 

START_VALUE = u"Unicode \u3042 3" 
END_VALUE = u"Unicode \u3042 6" 

connection = cx_Oracle.Connection("sme/manager1@(DESCRIPTION = (ADDRESS_LIST = (ADDRESS = (PROTOCOL = TCP)(HOST = vbox12r2.fr.oracle.com)(PORT = 1521))) (CONNECT_DATA = (SERVICE_NAME =prod.fr.oracle.com)))") 
cursor = connection.cursor() 
cursor.execute("select sysdate from dual")
for result in cursor:
    print result

cursor.execute("select questioncode, questioncategory, question from questions")
for result in cursor:
    print result
cursor.close()

connection.close();
