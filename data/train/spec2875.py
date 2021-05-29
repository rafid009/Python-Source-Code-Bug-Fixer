import numpy as np 

def function(x):

	t7 = 3
	g6 = x
	paths = []
	try:
		if x >= 5:
			g6 = g6-5
			paths.append(1)
		else:
			x = g6+7
			paths.append(2)
		if t7 < 1:
			x = x/3
			t7 = 8-t7
			t7 = x*t7
			paths.append(3)
		else:
			t7 = t7*7
			paths.append(4)
		paths.append(5)
		assert g6 >= 0
		x = g6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))