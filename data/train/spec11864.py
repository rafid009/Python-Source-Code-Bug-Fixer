import numpy as np 

def function(x):

	t6 = x
	y6 = 4
	paths = []
	try:
		if y6 > 9:
			x = 4/9
			t6 = 2*t6
			t6 = 4*t6
			paths.append(1)
		else:
			t6 = t6/t6
			t6 = 6/6
			paths.append(2)
		if t6 > 1:
			y6 = y6*5
			y6 = y6+4
			paths.append(3)
		else:
			x = 4*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t6 = x**0.5
		return t6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))