import MySQLdb

def get_all_states(username, password, database):
  """Connects to a MySQL server running on localhost at port 3306 and lists all states from the database hbtn_0e_0_usa, sorted in ascending order by states.id.

  Args:
    username: The MySQL username.
    password: The MySQL password.
    database: The database name.

  Returns:
    A list of tuples, where each tuple contains an integer state ID and a string state name.
  """

  connection = MySQLdb.connect(host='localhost', port=3306, user=username, passwd=password, db=database)
  cursor = connection.cursor()

  cursor.execute('SELECT id, name FROM states ORDER BY id ASC')
  states = cursor.fetchall()

  cursor.close()
  connection.close()

  return states

if __name__ == '__main__':
  username = input('Enter MySQL username: ')
  password = input('Enter MySQL password: ')
  database = input('Enter database name: ')

  states = get_all_states(username, password, database)

  for state in states:
    print(state)
