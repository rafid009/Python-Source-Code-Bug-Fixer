import numpy as np 

def function(x):

	i4 = x
	x2 = 4
	paths = []
	try:
		if i4 >= 7:
			x = i4+9
			paths.append(1)
		else:
			i4 = 8/i4
			i4 = 8+x
			x2 = 9/9
			paths.append(2)
		if i4 >= 1:
			x = i4*5
			x = 8/x
			x2 = i4-x2
			paths.append(3)
		else:
			i4 = 8*i4
			x = x*i4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x2 = x**0.5
		return x2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))