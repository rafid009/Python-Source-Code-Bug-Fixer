import numpy as np 

def function(x):

	a6 = 0
	m4 = 5
	paths = []
	try:
		if x >= 1:
			m4 = m4/x
			m4 = m4+m4
			m4 = 3-m4
			paths.append(1)
		else:
			x = 8*9
			paths.append(2)
		if a6 < 9:
			a6 = a6-a6
			paths.append(3)
		else:
			a6 = 8-m4
			paths.append(4)
		paths.append(5)
		assert m4 >= 0
		x = m4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))