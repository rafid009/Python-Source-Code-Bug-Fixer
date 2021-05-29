import numpy as np 

def function(x):

	i4 = x
	y3 = x
	paths = []
	try:
		if x < 1:
			x = x-9
			paths.append(1)
		else:
			i4 = 8+i4
			paths.append(2)
		if i4 <= 1:
			x = 6-0
			paths.append(3)
		else:
			i4 = x*i4
			x = x*y3
			paths.append(4)
		paths.append(5)
		assert y3 >= 0
		x = y3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))