import numpy as np 

def function(x):

	v7 = x
	f7 = x
	paths = []
	try:
		if x < 7:
			f7 = 1*f7
			paths.append(1)
		else:
			f7 = f7/2
			paths.append(2)
		if x < 4:
			v7 = 2+v7
			paths.append(3)
		else:
			x = x-x
			f7 = 6/f7
			paths.append(4)
		paths.append(5)
		assert f7 >= 0
		v7 = f7**0.5
		return v7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))