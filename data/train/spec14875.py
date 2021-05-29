import numpy as np 

def function(x):

	g0 = 6
	t6 = x
	paths = []
	try:
		if t6 > 8:
			t6 = t6/x
			g0 = 2/g0
			paths.append(1)
		else:
			x = 9+x
			paths.append(2)
		if x > 9:
			t6 = t6/x
			paths.append(3)
		else:
			g0 = g0*g0
			t6 = 1-x
			paths.append(4)
		paths.append(5)
		assert t6 >= 0
		t6 = t6**0.5
		return t6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))