import numpy as np 

def function(x):

	m4 = x
	o4 = x
	paths = []
	try:
		if o4 > 4:
			m4 = m4/x
			paths.append(1)
		else:
			m4 = 3+o4
			m4 = m4+4
			paths.append(2)
		if o4 >= 5:
			x = 6*9
			o4 = x-8
			paths.append(3)
		else:
			x = 0/x
			paths.append(4)
		paths.append(5)
		assert o4 >= 0
		m4 = o4**0.5
		return m4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))