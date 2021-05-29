import numpy as np 

def function(x):

	g3 = x
	e7 = x
	paths = []
	try:
		if x < 8:
			e7 = 6+0
			paths.append(1)
		else:
			x = e7/7
			paths.append(2)
		if g3 >= 5:
			x = x*3
			x = x-6
			e7 = 0+e7
			paths.append(3)
		else:
			x = x/8
			paths.append(4)
		paths.append(5)
		assert g3 >= 0
		g3 = g3**0.5
		return g3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))