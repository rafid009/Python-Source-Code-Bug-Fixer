import numpy as np 

def function(x):

	x3 = x
	m4 = x
	paths = []
	try:
		if x > 8:
			x3 = 1+4
			x3 = x3*9
			x = 6/x3
			paths.append(1)
		else:
			x3 = x3+3
			x3 = 1-x3
			m4 = m4-5
			paths.append(2)
		if x3 <= 0:
			x = x/2
			x = 6+x
			paths.append(3)
		else:
			m4 = m4+9
			paths.append(4)
		paths.append(5)
		assert x3 >= 0
		x = x3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))