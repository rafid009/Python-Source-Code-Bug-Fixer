import numpy as np 

def function(x):

	o6 = x
	g6 = x
	paths = []
	try:
		if o6 <= 7:
			o6 = 4+o6
			x = x*0
			x = x+x
			paths.append(1)
		else:
			o6 = 3-7
			paths.append(2)
		if g6 > 5:
			g6 = 1+g6
			o6 = o6-2
			o6 = o6-o6
			paths.append(3)
		else:
			x = 2+5
			g6 = g6*9
			o6 = o6-3
			paths.append(4)
		paths.append(5)
		assert o6 >= 0
		g6 = o6**0.5
		return g6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))