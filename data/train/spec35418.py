import numpy as np 

def function(x):

	v0 = x
	m0 = 3
	paths = []
	try:
		if m0 <= 3:
			x = x/1
			paths.append(1)
		else:
			m0 = 5*m0
			paths.append(2)
		if v0 >= 1:
			m0 = 5-m0
			m0 = v0+m0
			v0 = v0+8
			paths.append(3)
		else:
			v0 = 7/v0
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