import numpy as np 

def function(x):

	i0 = 8
	i6 = 5
	paths = []
	try:
		if x <= 8:
			x = 7*x
			i0 = 2*x
			x = x-i6
			paths.append(1)
		else:
			i6 = i6-x
			paths.append(2)
		if i0 > 4:
			i6 = x+i6
			paths.append(3)
		else:
			x = 1+0
			i6 = i6*6
			i6 = i6+i6
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