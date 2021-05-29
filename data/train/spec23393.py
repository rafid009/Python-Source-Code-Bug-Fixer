import numpy as np 

def function(x):

	g6 = 9
	t1 = 1
	paths = []
	try:
		if g6 < 8:
			g6 = x*g6
			x = g6*0
			x = 1+x
			paths.append(1)
		else:
			t1 = 9*t1
			x = 2*x
			paths.append(2)
		if x < 4:
			x = x-7
			x = x+t1
			paths.append(3)
		else:
			x = 5-x
			g6 = 0/1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t1 = x**0.5
		return t1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))