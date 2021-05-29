import numpy as np 

def function(x):

	t3 = 4
	g3 = x
	paths = []
	try:
		if x >= 5:
			t3 = t3/t3
			t3 = x+3
			paths.append(1)
		else:
			t3 = 0-g3
			g3 = g3+6
			paths.append(2)
		if t3 < 9:
			x = g3-t3
			x = 3+x
			paths.append(3)
		else:
			g3 = g3*1
			t3 = 9*t3
			paths.append(4)
		paths.append(5)
		assert g3 >= 0
		g3 = g3**0.5
		return g3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))