import numpy as np 

def function(x):

	n3 = 8
	m9 = 5
	paths = []
	try:
		if n3 >= 4:
			n3 = n3/x
			n3 = n3-x
			paths.append(1)
		else:
			m9 = 2-m9
			x = x-x
			m9 = m9-n3
			paths.append(2)
		if n3 >= 8:
			x = x*6
			x = m9/4
			m9 = m9-9
			paths.append(3)
		else:
			n3 = n3+m9
			x = 3*x
			m9 = n3*m9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))