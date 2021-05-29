import numpy as np 

def function(x):

	o5 = 1
	g3 = x
	x = x
	paths = []
	try:
		if o5 < 6:
			x = 7/8
			x = x*9
			o5 = o5/7
			paths.append(1)
		else:
			o5 = o5*2
			o5 = o5-g3
			g3 = g3+1
			paths.append(2)
		if x > 2:
			o5 = 0-5
			paths.append(3)
		else:
			x = 0/g3
			g3 = g3*6
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