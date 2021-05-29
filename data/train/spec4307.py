import numpy as np 

def function(x):

	y4 = 6
	m0 = 6
	x = x
	paths = []
	try:
		if m0 > 3:
			m0 = y4*0
			x = x*9
			paths.append(1)
		else:
			y4 = 5/y4
			paths.append(2)
		if m0 > 7:
			x = x*5
			paths.append(3)
		else:
			m0 = m0+8
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