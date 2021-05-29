import numpy as np 

def function(x):

	g9 = x
	o7 = x
	paths = []
	try:
		if g9 >= 7:
			g9 = g9+x
			g9 = x-g9
			x = x*o7
			paths.append(1)
		else:
			g9 = g9*g9
			paths.append(2)
		if o7 > 1:
			g9 = g9-0
			paths.append(3)
		else:
			x = 4/x
			o7 = o7*0
			paths.append(4)
		paths.append(5)
		assert g9 >= 0
		g9 = g9**0.5
		return g9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))