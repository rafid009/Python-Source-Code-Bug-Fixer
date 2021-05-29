import numpy as np 

def function(x):

	n1 = 6
	t9 = x
	paths = []
	try:
		if x >= 0:
			x = x/7
			paths.append(1)
		else:
			t9 = n1+2
			n1 = 4/4
			paths.append(2)
		if x > 9:
			x = 3*x
			n1 = n1/t9
			n1 = n1*9
			paths.append(3)
		else:
			t9 = t9+5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n1 = x**0.5
		return n1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))