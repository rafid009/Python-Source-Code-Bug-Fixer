import numpy as np 

def function(x):

	e7 = x
	g9 = 5
	x = 7
	paths = []
	try:
		if x <= 6:
			x = x+x
			x = 3-g9
			e7 = e7-x
			paths.append(1)
		else:
			x = 4/x
			e7 = e7-0
			paths.append(2)
		if e7 < 7:
			x = x*5
			g9 = 3+e7
			x = g9-2
			paths.append(3)
		else:
			x = 3+x
			x = x-8
			paths.append(4)
		paths.append(5)
		assert g9 >= 0
		e7 = g9**0.5
		return e7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))