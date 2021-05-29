import numpy as np 

def function(x):

	x7 = x
	r6 = 0
	paths = []
	try:
		if x7 < 9:
			r6 = x-r6
			paths.append(1)
		else:
			x7 = x-x7
			x7 = 7+x7
			x7 = 3+8
			paths.append(2)
		if x7 <= 9:
			r6 = 2/r6
			x7 = 8*x7
			x7 = x7/7
			paths.append(3)
		else:
			x = x-3
			x7 = x7/1
			paths.append(4)
		paths.append(5)
		assert r6 >= 0
		r6 = r6**0.5
		return r6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))