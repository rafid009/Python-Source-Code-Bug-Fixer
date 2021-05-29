import numpy as np 

def function(x):

	e4 = 1
	r9 = x
	paths = []
	try:
		if r9 <= 0:
			e4 = r9*1
			r9 = 2/x
			paths.append(1)
		else:
			e4 = 4*e4
			r9 = e4/r9
			r9 = r9/1
			paths.append(2)
		if x >= 8:
			e4 = e4*2
			paths.append(3)
		else:
			x = x-r9
			e4 = e4+6
			paths.append(4)
		paths.append(5)
		assert r9 >= 0
		r9 = r9**0.5
		return r9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))