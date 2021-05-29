import numpy as np 

def function(x):

	v5 = 5
	g3 = 5
	paths = []
	try:
		if g3 >= 5:
			v5 = 2-v5
			v5 = v5*v5
			paths.append(1)
		else:
			v5 = x*3
			g3 = g3-6
			x = 7/x
			paths.append(2)
		if g3 <= 8:
			g3 = g3-v5
			paths.append(3)
		else:
			v5 = 6-v5
			v5 = 0*v5
			paths.append(4)
		paths.append(5)
		assert g3 >= 0
		x = g3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))