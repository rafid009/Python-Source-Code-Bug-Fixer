import numpy as np 

def function(x):

	a7 = x
	v2 = x
	paths = []
	try:
		if v2 < 9:
			x = 3+3
			paths.append(1)
		else:
			x = 4*4
			a7 = x+9
			paths.append(2)
		if a7 < 7:
			x = 9-6
			v2 = v2*9
			paths.append(3)
		else:
			a7 = 3/6
			paths.append(4)
		paths.append(5)
		assert a7 >= 0
		v2 = a7**0.5
		return v2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))