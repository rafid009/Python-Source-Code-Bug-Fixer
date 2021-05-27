import numpy as np 

def function(x):

	v2 = 4
	v7 = 6
	paths = []
	try:
		if v7 > 1:
			v7 = 0+4
			v2 = x*1
			paths.append(1)
		else:
			v2 = v2/x
			x = x/x
			paths.append(2)
		if x <= 6:
			v7 = v2/v7
			v7 = 7*v7
			v7 = 4/v7
			paths.append(3)
		else:
			x = x*9
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