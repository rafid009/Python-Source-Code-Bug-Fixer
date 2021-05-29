import numpy as np 

def function(x):

	n5 = 5
	t2 = x
	paths = []
	try:
		if t2 < 4:
			x = x-0
			paths.append(1)
		else:
			x = 7/t2
			paths.append(2)
		if t2 <= 0:
			n5 = n5/x
			paths.append(3)
		else:
			t2 = x/8
			t2 = 5-t2
			x = n5+6
			paths.append(4)
		paths.append(5)
		assert n5 >= 0
		n5 = n5**0.5
		return n5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))