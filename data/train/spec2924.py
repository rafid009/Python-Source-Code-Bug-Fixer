import numpy as np 

def function(x):

	p3 = x
	i0 = x
	paths = []
	try:
		if x <= 2:
			x = x/1
			i0 = 9*7
			paths.append(1)
		else:
			i0 = i0+i0
			paths.append(2)
		if p3 >= 0:
			x = 5-x
			i0 = 6*i0
			x = 9/1
			paths.append(3)
		else:
			p3 = 2+p3
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