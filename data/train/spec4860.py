import numpy as np 

def function(x):

	n5 = 9
	t5 = 6
	paths = []
	try:
		if x < 9:
			n5 = n5*n5
			paths.append(1)
		else:
			t5 = 7-1
			n5 = n5*x
			x = 5*x
			paths.append(2)
		if t5 <= 7:
			t5 = 4-3
			paths.append(3)
		else:
			t5 = 6-t5
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