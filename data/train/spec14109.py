import numpy as np 

def function(x):

	t6 = 2
	g1 = x
	paths = []
	try:
		if t6 > 5:
			g1 = 7+g1
			t6 = 3*t6
			g1 = 2*9
			paths.append(1)
		else:
			t6 = t6+t6
			x = x/7
			t6 = t6/x
			paths.append(2)
		if t6 < 1:
			t6 = 4*t6
			g1 = 3+g1
			x = x+2
			paths.append(3)
		else:
			g1 = 9-g1
			t6 = t6*5
			x = t6-x
			paths.append(4)
		paths.append(5)
		assert t6 >= 0
		x = t6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))