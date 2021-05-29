import numpy as np 

def function(x):

	v9 = 5
	v1 = x
	paths = []
	try:
		if v9 < 9:
			v9 = 0-v1
			x = 1+x
			v1 = v1-1
			paths.append(1)
		else:
			x = x*8
			v9 = v9/9
			paths.append(2)
		if v1 >= 5:
			v9 = v9*4
			v1 = x/7
			v1 = x-v1
			paths.append(3)
		else:
			x = x*v9
			v9 = v9/7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v9 = x**0.5
		return v9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))