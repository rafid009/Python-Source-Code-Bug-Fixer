import numpy as np 

def function(x):

	g3 = x
	k4 = 7
	paths = []
	try:
		if x <= 4:
			x = x*g3
			paths.append(1)
		else:
			g3 = 4-g3
			paths.append(2)
		if g3 > 6:
			g3 = 7-k4
			x = x+g3
			g3 = 4+k4
			paths.append(3)
		else:
			x = 7/x
			g3 = x*g3
			k4 = 9/k4
			paths.append(4)
		paths.append(5)
		assert g3 >= 0
		k4 = g3**0.5
		return k4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))