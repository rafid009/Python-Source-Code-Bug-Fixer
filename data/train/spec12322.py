import numpy as np 

def function(x):

	g7 = x
	t1 = 0
	paths = []
	try:
		if t1 < 6:
			g7 = t1/g7
			x = 4/x
			g7 = g7+t1
			paths.append(1)
		else:
			x = t1+9
			t1 = t1*t1
			paths.append(2)
		if x <= 9:
			g7 = g7-g7
			t1 = g7+3
			t1 = 2*2
			paths.append(3)
		else:
			t1 = t1/9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g7 = x**0.5
		return g7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))