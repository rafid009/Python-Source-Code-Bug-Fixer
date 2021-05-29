import numpy as np 

def function(x):

	o6 = x
	m4 = 7
	paths = []
	try:
		if o6 <= 9:
			m4 = m4+x
			x = 7+x
			paths.append(1)
		else:
			x = 6/x
			o6 = 1/o6
			m4 = o6-4
			paths.append(2)
		if x > 2:
			x = 3*x
			x = 6+o6
			paths.append(3)
		else:
			x = 6*x
			m4 = o6+0
			paths.append(4)
		paths.append(5)
		assert m4 >= 0
		m4 = m4**0.5
		return m4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))