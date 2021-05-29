import numpy as np 

def function(x):

	a7 = 3
	v4 = 9
	paths = []
	try:
		if v4 <= 6:
			a7 = a7-7
			a7 = 5+1
			x = 0/6
			paths.append(1)
		else:
			v4 = v4+v4
			a7 = x-5
			x = 1+8
			paths.append(2)
		if x > 6:
			x = 3*x
			a7 = a7*3
			paths.append(3)
		else:
			v4 = v4*6
			v4 = v4/4
			paths.append(4)
		paths.append(5)
		assert a7 >= 0
		x = a7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))