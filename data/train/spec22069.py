import numpy as np 

def function(x):

	e3 = x
	i7 = 2
	paths = []
	try:
		if x > 3:
			x = x+7
			x = 9-4
			paths.append(1)
		else:
			e3 = e3*9
			x = x-i7
			paths.append(2)
		if i7 < 4:
			e3 = 1*e3
			paths.append(3)
		else:
			x = 1-x
			x = 0*2
			x = x*6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i7 = x**0.5
		return i7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))