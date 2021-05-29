import numpy as np 

def function(x):

	t3 = 5
	g3 = 7
	paths = []
	try:
		if t3 <= 4:
			x = x*x
			g3 = 9*6
			t3 = g3/4
			paths.append(1)
		else:
			t3 = t3-g3
			paths.append(2)
		if x <= 6:
			g3 = g3+1
			g3 = 3*g3
			g3 = g3+1
			paths.append(3)
		else:
			x = 6*8
			g3 = 3*g3
			t3 = 7/4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t3 = x**0.5
		return t3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))