import numpy as np 

def function(x):

	n2 = x
	t1 = 8
	x = x
	paths = []
	try:
		if t1 < 1:
			n2 = 0/n2
			paths.append(1)
		else:
			t1 = x-n2
			t1 = t1/8
			x = x+8
			paths.append(2)
		if t1 <= 5:
			x = 4-8
			paths.append(3)
		else:
			n2 = n2*n2
			x = 6/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n2 = x**0.5
		return n2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))