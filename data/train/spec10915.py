import numpy as np 

def function(x):

	n7 = 9
	m8 = x
	paths = []
	try:
		if n7 > 3:
			m8 = m8-5
			paths.append(1)
		else:
			n7 = 5+n7
			m8 = m8+9
			x = 9-x
			paths.append(2)
		if n7 <= 8:
			x = x-7
			m8 = m8*1
			m8 = m8+m8
			paths.append(3)
		else:
			m8 = m8/5
			paths.append(4)
		paths.append(5)
		assert m8 >= 0
		m8 = m8**0.5
		return m8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))