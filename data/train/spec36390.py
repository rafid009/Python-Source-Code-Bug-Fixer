import numpy as np 

def function(x):

	e4 = 9
	g9 = 9
	x = x
	paths = []
	try:
		if g9 <= 5:
			x = 4/x
			paths.append(1)
		else:
			e4 = 1+e4
			g9 = 8-g9
			paths.append(2)
		if x < 4:
			g9 = 2+g9
			paths.append(3)
		else:
			x = 6+4
			paths.append(4)
		paths.append(5)
		assert g9 >= 0
		e4 = g9**0.5
		return e4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))