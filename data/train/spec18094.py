import numpy as np 

def function(x):

	f5 = 3
	v7 = x
	paths = []
	try:
		if v7 >= 9:
			v7 = v7/5
			v7 = v7/v7
			v7 = v7+v7
			paths.append(1)
		else:
			v7 = x*f5
			paths.append(2)
		if x > 6:
			f5 = f5/7
			f5 = 2*f5
			paths.append(3)
		else:
			f5 = 5-f5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v7 = x**0.5
		return v7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))