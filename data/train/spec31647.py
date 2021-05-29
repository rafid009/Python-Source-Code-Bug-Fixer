import numpy as np 

def function(x):

	r1 = 3
	i8 = 6
	paths = []
	try:
		if r1 > 4:
			r1 = r1+6
			x = i8-x
			paths.append(1)
		else:
			i8 = i8+i8
			x = x*8
			paths.append(2)
		if r1 <= 6:
			r1 = r1*x
			r1 = r1*8
			paths.append(3)
		else:
			x = 9+7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r1 = x**0.5
		return r1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))