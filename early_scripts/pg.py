import psycopg2
from psycopg2 import Error


create_table_sql = '''
	CREATE TABLE colleges_ca
	(ID		INT		PRIMARY KEY		NOT NULL,
	NAME	TEXT	NOT NULL,
	CITY	TEXT	NOT NULL,
	STATE	TEXT	NOT NULL,
	ZIP		INT		NOT NULL,
	URL		TEXT	NOT NULL,
	ADM_RATE	REAL	NOT NULL,
	SATVR25		INT		NOT NULL,
	SATVR75		INT		NOT NULL,
	SATMT25		INT		NOT NULL,
	SATMT75		INT		NOT NULL,
	SATWR25		INT		NOT NULL,
	SATWR75		INT		NOT NULL,
	SATVRMID	INT		NOT NULL,
	SATMTMID	INT		NOT NULL,
	ACTCM25		INT		NOT NULL,
	ACTCM75		INT		NOT NULL,
	ACTEN25		INT		NOT NULL,
	ACTEN75		INT		NOT NULL,
	ACTMT25		INT		NOT NULL,
	ACTMT75		INT		NOT NULL,
	ACTWR25		INT		NOT NULL,
	ACTWR75		INT		NOT NULL,
	ACTCMMID	INT		NOT NULL,
	ACTENMID	INT		NOT NULL,
	ACTMTMID	INT		NOT NULL,
	ACTWRMID	INT		NOT NULL,
	SAT_AVG		INT		NOT NULL,
	TUITION_IN	INT		NOT NULL,
	TUITION_OUT	INT		NOT NULL
	);
''' 



def create_table_pg(sql, credentials):
	
	try:
		connection = psycopg2.connect(
			user = credentials['user'],
			password = credentials['password'],
			host = credentials['host'],
			port = credentials['port'],
			database = credentials['database']
		)
		
		cursor = connection.cursor()
		cursor.execute(sql)
		connection.commit()
		print("Table created successfully in PostgreSQL")
	
	except (Exception, psycopg2.DatabaseError) as error:
		print("Error while creating PostgreSQL table", error)
	
	finally:
		if(connection):
			cursor.close()
			connection.close()
			print("PostgreSQL connection is closed")
