import numpy as np 

def function(x):

	n4 = x
	t8 = x
	paths = []
	try:
		if n4 > 9:
			t8 = t8/t8
			x = 8-n4
			paths.append(1)
		else:
			t8 = 6+6
			paths.append(2)
		if x > 5:
			x = 6*8
			paths.append(3)
		else:
			x = x-x
			paths.append(4)
		paths.append(5)
		assert n4 >= 0
		n4 = n4**0.5
		return n4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))