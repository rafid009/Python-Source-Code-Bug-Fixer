import numpy as np 

def function(x):

	e3 = 4
	i9 = x
	paths = []
	try:
		if e3 <= 0:
			i9 = i9-6
			paths.append(1)
		else:
			i9 = i9/1
			x = x-7
			paths.append(2)
		if x < 1:
			e3 = i9*e3
			i9 = i9/i9
			paths.append(3)
		else:
			x = x*e3
			paths.append(4)
		paths.append(5)
		assert e3 >= 0
		x = e3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))