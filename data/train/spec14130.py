import numpy as np 

def function(x):

	v7 = 3
	v6 = 6
	paths = []
	try:
		if v6 < 6:
			v7 = 1+v7
			v6 = 8*8
			paths.append(1)
		else:
			x = x*v7
			paths.append(2)
		if x < 8:
			v7 = v7*v7
			x = 0+8
			v6 = x/9
			paths.append(3)
		else:
			x = 8-x
			v7 = v7-5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v6 = x**0.5
		return v6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))