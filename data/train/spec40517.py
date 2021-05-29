import numpy as np 

def function(x):

	i6 = x
	x7 = x
	paths = []
	try:
		if x7 < 7:
			i6 = i6+2
			paths.append(1)
		else:
			i6 = 0/x
			x = x-x
			paths.append(2)
		if x7 >= 1:
			i6 = i6*i6
			x = x*2
			paths.append(3)
		else:
			x = 7+x
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