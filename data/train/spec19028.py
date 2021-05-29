import numpy as np 

def function(x):

	n5 = 4
	t4 = 3
	paths = []
	try:
		if x <= 5:
			t4 = t4*7
			x = 5+4
			n5 = 2-t4
			paths.append(1)
		else:
			t4 = 2/2
			paths.append(2)
		if x <= 8:
			x = n5*n5
			paths.append(3)
		else:
			t4 = 4*1
			n5 = 5/n5
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