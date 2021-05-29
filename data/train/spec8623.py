import numpy as np 

def function(x):

	m0 = 9
	y3 = 1
	paths = []
	try:
		if y3 < 5:
			y3 = y3/4
			paths.append(1)
		else:
			x = x*y3
			paths.append(2)
		if x < 5:
			y3 = 8-y3
			m0 = 5-m0
			paths.append(3)
		else:
			x = x+0
			x = x/1
			m0 = 7*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y3 = x**0.5
		return y3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))