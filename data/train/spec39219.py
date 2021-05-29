import numpy as np 

def function(x):

	o7 = x
	e8 = 5
	x = 6
	paths = []
	try:
		if o7 > 3:
			e8 = e8-6
			paths.append(1)
		else:
			o7 = 0*e8
			e8 = e8+1
			paths.append(2)
		if o7 <= 2:
			o7 = 4-e8
			paths.append(3)
		else:
			e8 = 3/e8
			e8 = o7+7
			e8 = 3-x
			paths.append(4)
		paths.append(5)
		assert o7 >= 0
		x = o7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))