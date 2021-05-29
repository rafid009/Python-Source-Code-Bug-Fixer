import numpy as np 

def function(x):

	i9 = x
	a8 = x
	x = x
	paths = []
	try:
		if x > 3:
			x = i9/5
			paths.append(1)
		else:
			x = 8/4
			x = x-5
			i9 = 9-i9
			paths.append(2)
		if x <= 8:
			x = 2*a8
			paths.append(3)
		else:
			i9 = 5*i9
			paths.append(4)
		paths.append(5)
		assert a8 >= 0
		x = a8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))