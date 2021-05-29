import numpy as np 

def function(x):

	t9 = x
	n1 = 1
	paths = []
	try:
		if t9 < 5:
			t9 = t9+6
			n1 = n1-t9
			n1 = n1+t9
			paths.append(1)
		else:
			n1 = 3-5
			t9 = n1+x
			x = 0+x
			paths.append(2)
		if x > 7:
			n1 = 7+n1
			paths.append(3)
		else:
			x = 6*x
			t9 = 1/8
			n1 = n1*6
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