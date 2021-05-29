import numpy as np 

def function(x):

	t1 = 9
	x2 = x
	paths = []
	try:
		if x2 < 1:
			x = x+6
			x = 1*x
			paths.append(1)
		else:
			x = x+x2
			paths.append(2)
		if x > 4:
			x = x+9
			t1 = t1+0
			x2 = 3-x2
			paths.append(3)
		else:
			x2 = x2/x
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