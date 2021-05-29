import numpy as np 

def function(x):

	t3 = 0
	n6 = 5
	paths = []
	try:
		if x >= 5:
			n6 = 6/n6
			n6 = 3+x
			paths.append(1)
		else:
			n6 = t3+n6
			paths.append(2)
		if t3 > 0:
			t3 = 6/t3
			paths.append(3)
		else:
			t3 = t3*7
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