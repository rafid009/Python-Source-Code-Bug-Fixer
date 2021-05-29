import numpy as np 

def function(x):

	a9 = 0
	t4 = x
	paths = []
	try:
		if t4 <= 8:
			a9 = a9/x
			paths.append(1)
		else:
			x = 0+x
			paths.append(2)
		if x <= 9:
			x = x/1
			t4 = t4+9
			paths.append(3)
		else:
			x = x-5
			t4 = t4*x
			a9 = 3*x
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