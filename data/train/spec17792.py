import numpy as np 

def function(x):

	e6 = 1
	f8 = x
	paths = []
	try:
		if f8 <= 1:
			x = 7-5
			e6 = f8-4
			paths.append(1)
		else:
			e6 = 6*e6
			paths.append(2)
		if f8 <= 2:
			f8 = 9-f8
			x = 4*9
			e6 = e6+x
			paths.append(3)
		else:
			e6 = 9-2
			f8 = f8-2
			e6 = 6-e6
			paths.append(4)
		paths.append(5)
		assert e6 >= 0
		x = e6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))