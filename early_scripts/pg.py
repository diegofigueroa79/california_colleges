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
			

def insert_bulk_data(ls, credentials):
	
	try:
		connection = psycopg2.connect(
			user = credentials['user'],
			password = credentials['password'],
			host = credentials['host'],
			port = credentials['port'],
			database = credentials['database']
		)
		
		cursor = connection.cursor()
		
		records_list_template = ','.join(['%s'] * len(ls))
		
		insert_query = 'INSERT INTO colleges_ca\
			(NAME, CITY, STATE, ZIP, URL, ADM_RATE,\
			SATVR25, SATVR75, SATMT25, SATMT75,\
			SATWR25, SATWR75, SATVRMID, SATMTMID, ACTCM25,\
			ACTCM75, ACTEN25, ACTEN75, ACTMT25, ACTMT75,\
			ACTWR25, ACTWR75, ACTCMMID, ACTENMID, ACTMTMID,\
			ACTWRMID, SAT_AVG, TUITION_IN, TUITION_OUT)\
			VALUES {}'.format(records_list_template)
		
		cursor.execute(insert_query, ls)
		connection.commit()
	
	except (Exception, psycopg2.Error) as error:
		if(connection):
			print("Failed to insert record into mobile table", error)
	
	finally:
		if(connection):
			cursor.close()
			connection.close()
			print("PostgreSQL connection is closed")
		
		
		
