import numpy as np 

def function(x):

	t6 = x
	g1 = x
	paths = []
	try:
		if x <= 3:
			g1 = g1/g1
			t6 = x+3
			paths.append(1)
		else:
			g1 = g1-7
			paths.append(2)
		if x > 0:
			g1 = g1/t6
			paths.append(3)
		else:
			t6 = x+8
			t6 = t6+5
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