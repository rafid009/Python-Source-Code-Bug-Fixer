import numpy as np 

def function(x):

	a5 = x
	v2 = 6
	paths = []
	try:
		if a5 < 1:
			a5 = a5/1
			paths.append(1)
		else:
			v2 = 4*9
			x = 5*v2
			a5 = 1*a5
			paths.append(2)
		if v2 < 0:
			v2 = v2-6
			a5 = 2/a5
			a5 = 3-7
			paths.append(3)
		else:
			x = 7/x
			paths.append(4)
		paths.append(5)
		assert a5 >= 0
		x = a5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))