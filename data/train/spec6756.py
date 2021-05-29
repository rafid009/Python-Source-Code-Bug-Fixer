import numpy as np 

def function(x):

	o5 = x
	g9 = x
	x = 0
	paths = []
	try:
		if o5 < 3:
			g9 = g9-7
			o5 = 2+o5
			x = 9*x
			paths.append(1)
		else:
			o5 = 5+7
			paths.append(2)
		if g9 <= 6:
			o5 = 1+o5
			paths.append(3)
		else:
			o5 = o5-x
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