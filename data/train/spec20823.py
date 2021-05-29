import numpy as np 

def function(x):

	e5 = 9
	g9 = 3
	paths = []
	try:
		if x <= 9:
			e5 = e5/x
			e5 = 8-8
			g9 = x+g9
			paths.append(1)
		else:
			g9 = g9/7
			g9 = g9-0
			paths.append(2)
		if g9 < 8:
			g9 = 0+g9
			paths.append(3)
		else:
			e5 = e5/2
			e5 = x-e5
			e5 = 3-e5
			paths.append(4)
		paths.append(5)
		assert g9 >= 0
		e5 = g9**0.5
		return e5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))