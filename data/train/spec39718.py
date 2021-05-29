import numpy as np 

def function(x):

	g1 = x
	v9 = x
	paths = []
	try:
		if v9 < 3:
			x = x-g1
			paths.append(1)
		else:
			v9 = 1+v9
			g1 = 2+0
			v9 = 7-1
			paths.append(2)
		if x > 0:
			g1 = 7-2
			paths.append(3)
		else:
			v9 = g1-x
			paths.append(4)
		paths.append(5)
		assert g1 >= 0
		v9 = g1**0.5
		return v9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))