import numpy as np 

def function(x):

	t4 = 5
	g7 = x
	paths = []
	try:
		if x >= 1:
			x = t4-1
			g7 = 4*x
			paths.append(1)
		else:
			x = x+t4
			x = x/5
			t4 = g7/8
			paths.append(2)
		if t4 > 2:
			x = x-t4
			paths.append(3)
		else:
			g7 = g7*g7
			x = x+3
			t4 = 3/6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t4 = x**0.5
		return t4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))