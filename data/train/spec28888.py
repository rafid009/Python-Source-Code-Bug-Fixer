import numpy as np 

def function(x):

	g2 = 3
	e9 = 4
	x = x
	paths = []
	try:
		if x <= 4:
			e9 = 5+e9
			paths.append(1)
		else:
			g2 = g2+9
			g2 = 4-g2
			x = 6+x
			paths.append(2)
		if x <= 6:
			x = x*6
			e9 = 9*e9
			paths.append(3)
		else:
			e9 = 7-7
			x = e9-g2
			e9 = e9/2
			paths.append(4)
		paths.append(5)
		assert g2 >= 0
		e9 = g2**0.5
		return e9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))