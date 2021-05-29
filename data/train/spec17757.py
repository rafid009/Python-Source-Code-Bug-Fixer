import numpy as np 

def function(x):

	t1 = 1
	n6 = x
	paths = []
	try:
		if x > 1:
			x = x*x
			x = x*7
			paths.append(1)
		else:
			n6 = n6*6
			paths.append(2)
		if t1 > 0:
			n6 = 8+x
			t1 = t1/t1
			paths.append(3)
		else:
			n6 = n6/3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n6 = x**0.5
		return n6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))