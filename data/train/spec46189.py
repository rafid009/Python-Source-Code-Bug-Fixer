import numpy as np 

def function(x):

	m5 = x
	m8 = x
	paths = []
	try:
		if x <= 5:
			m5 = m5*2
			m8 = 9*m8
			m8 = 5+4
			paths.append(1)
		else:
			x = 5-x
			m8 = x*m8
			paths.append(2)
		if x >= 0:
			x = 9-m5
			m5 = m5*5
			m5 = m5+m8
			paths.append(3)
		else:
			m5 = m5+1
			paths.append(4)
		paths.append(5)
		assert m5 >= 0
		m5 = m5**0.5
		return m5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))