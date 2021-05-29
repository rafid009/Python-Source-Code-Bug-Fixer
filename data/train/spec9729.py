import numpy as np 

def function(x):

	d6 = 9
	g9 = x
	paths = []
	try:
		if g9 > 5:
			g9 = g9-d6
			x = g9/x
			paths.append(1)
		else:
			g9 = d6*g9
			d6 = 4-g9
			paths.append(2)
		if g9 < 7:
			x = x/x
			paths.append(3)
		else:
			x = x/2
			paths.append(4)
		paths.append(5)
		assert g9 >= 0
		d6 = g9**0.5
		return d6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))