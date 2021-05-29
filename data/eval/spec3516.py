import numpy as np 

def function(x):

	m9 = 4
	m8 = x
	paths = []
	try:
		if m9 > 3:
			x = 5*x
			m9 = 8-5
			x = x*0
			paths.append(1)
		else:
			x = x-m9
			paths.append(2)
		if x >= 8:
			m9 = 4-m9
			x = m9*m9
			paths.append(3)
		else:
			m9 = 5/m9
			x = x*m8
			paths.append(4)
		paths.append(5)
		assert m8 >= 0
		m9 = m8**0.5
		return m9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))