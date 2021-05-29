import numpy as np 

def function(x):

	t1 = x
	n6 = 4
	paths = []
	try:
		if t1 <= 7:
			n6 = n6/x
			t1 = 1/4
			t1 = t1+6
			paths.append(1)
		else:
			t1 = 1+t1
			paths.append(2)
		if n6 < 8:
			t1 = 9+6
			t1 = n6-t1
			n6 = t1-n6
			paths.append(3)
		else:
			x = x+0
			n6 = n6-6
			t1 = 1+n6
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