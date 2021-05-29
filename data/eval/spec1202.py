import numpy as np 

def function(x):

	t4 = x
	n5 = x
	paths = []
	try:
		if t4 < 6:
			x = 2-x
			t4 = 0/6
			paths.append(1)
		else:
			x = x/t4
			t4 = 8-t4
			paths.append(2)
		if t4 > 1:
			x = x/3
			paths.append(3)
		else:
			t4 = 3-t4
			n5 = 1/5
			n5 = x/2
			paths.append(4)
		paths.append(5)
		assert n5 >= 0
		x = n5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))