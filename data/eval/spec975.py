import numpy as np 

def function(x):

	g9 = x
	r9 = 8
	paths = []
	try:
		if g9 >= 1:
			g9 = g9/r9
			paths.append(1)
		else:
			x = 8*3
			x = g9+r9
			r9 = r9-4
			paths.append(2)
		if r9 > 7:
			r9 = 3-x
			x = 3/3
			paths.append(3)
		else:
			x = x+1
			paths.append(4)
		paths.append(5)
		assert g9 >= 0
		r9 = g9**0.5
		return r9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))