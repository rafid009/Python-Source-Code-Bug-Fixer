import numpy as np 

def function(x):

	d1 = x
	g0 = 8
	paths = []
	try:
		if x < 5:
			x = x+7
			g0 = 2+d1
			paths.append(1)
		else:
			g0 = 4/1
			x = x+x
			paths.append(2)
		if d1 >= 4:
			d1 = g0-6
			x = 6*0
			d1 = 8+9
			paths.append(3)
		else:
			d1 = d1+x
			paths.append(4)
		paths.append(5)
		assert d1 >= 0
		g0 = d1**0.5
		return g0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))