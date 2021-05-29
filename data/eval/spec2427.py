import numpy as np 

def function(x):

	d9 = 7
	i1 = x
	paths = []
	try:
		if d9 > 2:
			i1 = 1+3
			paths.append(1)
		else:
			i1 = 2+i1
			x = 6+9
			paths.append(2)
		if x >= 6:
			i1 = x+1
			d9 = 1/1
			d9 = 6*6
			paths.append(3)
		else:
			d9 = 0/2
			i1 = i1-3
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