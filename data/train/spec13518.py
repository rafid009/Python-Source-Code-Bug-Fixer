import numpy as np 

def function(x):

	t4 = 3
	n3 = 6
	paths = []
	try:
		if t4 > 6:
			x = t4/x
			n3 = n3/7
			x = x*7
			paths.append(1)
		else:
			t4 = t4*x
			paths.append(2)
		if t4 <= 6:
			n3 = 9/n3
			x = 3-x
			x = x-t4
			paths.append(3)
		else:
			n3 = 1*3
			t4 = 4-n3
			paths.append(4)
		paths.append(5)
		assert t4 >= 0
		n3 = t4**0.5
		return n3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))