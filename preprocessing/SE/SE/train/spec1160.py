import numpy as np 

def function(x):

	g3 = x
	d4 = 0
	paths = []
	try:
		if g3 > 9:
			x = 4/3
			d4 = 7+1
			g3 = 7-1
			paths.append(1)
		else:
			x = x+7
			x = x*9
			paths.append(2)
		if x < 2:
			d4 = d4+4
			d4 = 5+x
			paths.append(3)
		else:
			g3 = 9*9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d4 = x**0.5
		return d4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))