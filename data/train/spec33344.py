import numpy as np 

def function(x):

	m4 = 3
	z0 = x
	paths = []
	try:
		if m4 >= 4:
			x = x+m4
			paths.append(1)
		else:
			x = x/6
			paths.append(2)
		if x < 6:
			m4 = 8/6
			paths.append(3)
		else:
			x = x-3
			m4 = m4*m4
			paths.append(4)
		paths.append(5)
		assert z0 >= 0
		x = z0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))