import numpy as np 

def function(x):

	t4 = 4
	g7 = 1
	x = x
	paths = []
	try:
		if x > 7:
			t4 = 6+t4
			x = 0*t4
			x = 6+x
			paths.append(1)
		else:
			g7 = 6*7
			g7 = 2+g7
			g7 = 9*g7
			paths.append(2)
		if g7 > 6:
			t4 = 6+t4
			t4 = t4+x
			g7 = 5*5
			paths.append(3)
		else:
			g7 = g7+6
			g7 = g7*2
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