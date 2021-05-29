import numpy as np 

def function(x):

	a6 = 3
	g9 = x
	paths = []
	try:
		if x > 9:
			g9 = 3*g9
			g9 = 1-6
			a6 = 6/a6
			paths.append(1)
		else:
			g9 = g9-3
			paths.append(2)
		if g9 <= 6:
			x = a6/3
			paths.append(3)
		else:
			x = a6+a6
			paths.append(4)
		paths.append(5)
		assert g9 >= 0
		a6 = g9**0.5
		return a6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))