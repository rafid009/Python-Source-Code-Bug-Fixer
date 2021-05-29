import numpy as np 

def function(x):

	x1 = x
	m3 = x
	paths = []
	try:
		if x > 4:
			x1 = x1+x1
			paths.append(1)
		else:
			x1 = x*x1
			paths.append(2)
		if x < 4:
			x1 = 3+m3
			paths.append(3)
		else:
			m3 = 6*5
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