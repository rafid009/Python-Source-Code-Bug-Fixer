import numpy as np 

def function(x):

	o4 = 4
	g9 = x
	paths = []
	try:
		if g9 <= 8:
			g9 = g9/1
			paths.append(1)
		else:
			g9 = g9-o4
			x = g9*5
			x = 4+6
			paths.append(2)
		if x < 9:
			x = x*o4
			x = 0+x
			x = x*6
			paths.append(3)
		else:
			g9 = 8+o4
			paths.append(4)
		paths.append(5)
		assert g9 >= 0
		x = g9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))