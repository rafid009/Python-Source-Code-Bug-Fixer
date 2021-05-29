import numpy as np 

def function(x):

	n3 = x
	t4 = 5
	paths = []
	try:
		if n3 >= 9:
			n3 = 5+n3
			paths.append(1)
		else:
			t4 = 1*x
			t4 = 8/t4
			paths.append(2)
		if t4 >= 3:
			n3 = 6+7
			paths.append(3)
		else:
			t4 = 0*t4
			t4 = t4*5
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