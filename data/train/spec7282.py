import numpy as np 

def function(x):

	t7 = x
	g9 = x
	paths = []
	try:
		if t7 > 1:
			g9 = 5*g9
			t7 = 4+8
			paths.append(1)
		else:
			t7 = x*t7
			g9 = x-x
			t7 = g9+t7
			paths.append(2)
		if t7 >= 6:
			g9 = 4-g9
			t7 = x*x
			paths.append(3)
		else:
			t7 = t7*t7
			paths.append(4)
		paths.append(5)
		assert g9 >= 0
		x = g9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))