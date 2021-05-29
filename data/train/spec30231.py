import numpy as np 

def function(x):

	r6 = 8
	v4 = 9
	paths = []
	try:
		if r6 >= 9:
			r6 = r6+x
			v4 = v4-r6
			x = x-5
			paths.append(1)
		else:
			v4 = 4/8
			v4 = 3+6
			paths.append(2)
		if v4 < 0:
			x = x-x
			paths.append(3)
		else:
			x = x+6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r6 = x**0.5
		return r6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))