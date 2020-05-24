import psycopg2
from psycopg2 import Error


create_table_sql = '''
	CREATE TABLE colleges_ca
	(NAME	TEXT	PRIMARY KEY		NOT NULL,
	CITY	TEXT	NOT NULL,
	STATE	TEXT	NOT NULL,
	ZIP		TEXT	NOT NULL,
	URL		TEXT	NOT NULL,
	ADM_RATE	REAL	NOT NULL,
	SATVR25		REAL	NOT NULL,
	SATVR75		REAL	NOT NULL,
	SATMT25		REAL	NOT NULL,
	SATMT75		REAL	NOT NULL,
	SATWR25		REAL	NOT NULL,
	SATWR75		REAL	NOT NULL,
	SATVRMID	REAL	NOT NULL,
	SATMTMID	REAL	NOT NULL,
	ACTCM25		REAL	NOT NULL,
	ACTCM75		REAL	NOT NULL,
	ACTEN25		REAL	NOT NULL,
	ACTEN75		REAL	NOT NULL,
	ACTMT25		REAL	NOT NULL,
	ACTMT75		REAL	NOT NULL,
	ACTWR25		REAL	NOT NULL,
	ACTWR75		REAL	NOT NULL,
	ACTCMMID	REAL	NOT NULL,
	ACTENMID	REAL	NOT NULL,
	ACTMTMID	REAL	NOT NULL,
	ACTWRMID	REAL	NOT NULL,
	SAT_AVG		REAL	NOT NULL,
	TUITION_IN	REAL	NOT NULL,
	TUITION_OUT	REAL	NOT NULL
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
			VALUES {};'.format(records_list_template)
		#print(cursor.mogrify(insert_query, ls))
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
		
		
		
