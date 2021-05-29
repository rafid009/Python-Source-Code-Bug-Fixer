import numpy as np 

def function(x):

	r9 = x
	g6 = 9
	paths = []
	try:
		if r9 <= 4:
			g6 = 4/r9
			paths.append(1)
		else:
			r9 = r9/5
			x = x+6
			paths.append(2)
		if r9 > 5:
			x = x-x
			r9 = 3-6
			paths.append(3)
		else:
			x = 7/x
			g6 = 1-3
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