import numpy as np 

def function(x):

	t5 = 6
	g3 = x
	paths = []
	try:
		if g3 > 5:
			t5 = t5-8
			paths.append(1)
		else:
			g3 = g3-5
			x = g3-8
			x = 1/3
			paths.append(2)
		if g3 >= 2:
			g3 = 7/g3
			g3 = 0*9
			t5 = 3+t5
			paths.append(3)
		else:
			x = g3+7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))