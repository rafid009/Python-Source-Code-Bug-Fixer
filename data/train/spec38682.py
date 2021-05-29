import numpy as np 

def function(x):

	t6 = 2
	n7 = 6
	paths = []
	try:
		if t6 > 6:
			t6 = 3/7
			paths.append(1)
		else:
			n7 = 9+1
			n7 = n7/2
			paths.append(2)
		if x > 7:
			x = n7-x
			paths.append(3)
		else:
			n7 = 7/5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n7 = x**0.5
		return n7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))