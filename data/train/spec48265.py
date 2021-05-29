import numpy as np 

def function(x):

	j0 = 1
	g0 = x
	paths = []
	try:
		if g0 > 8:
			x = 7+x
			g0 = 0*3
			x = j0/x
			paths.append(1)
		else:
			j0 = j0-5
			j0 = j0/5
			paths.append(2)
		if g0 > 8:
			j0 = 9/j0
			x = x+g0
			paths.append(3)
		else:
			g0 = x+g0
			paths.append(4)
		paths.append(5)
		assert g0 >= 0
		j0 = g0**0.5
		return j0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))