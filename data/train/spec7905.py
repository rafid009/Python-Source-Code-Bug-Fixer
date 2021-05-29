import numpy as np 

def function(x):

	g3 = x
	a3 = x
	x = x
	paths = []
	try:
		if g3 <= 9:
			a3 = 8-x
			a3 = 6*a3
			paths.append(1)
		else:
			a3 = 4-g3
			a3 = 2+a3
			a3 = a3/a3
			paths.append(2)
		if x > 4:
			g3 = 7+g3
			paths.append(3)
		else:
			x = x/7
			paths.append(4)
		paths.append(5)
		assert g3 >= 0
		a3 = g3**0.5
		return a3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))