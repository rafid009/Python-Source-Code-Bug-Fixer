import numpy as np 

def function(x):

	n9 = 6
	t4 = x
	x = 8
	paths = []
	try:
		if t4 <= 8:
			t4 = 7/t4
			paths.append(1)
		else:
			t4 = t4*7
			n9 = n9*4
			n9 = t4+n9
			paths.append(2)
		if t4 < 1:
			x = t4+t4
			n9 = n9+2
			paths.append(3)
		else:
			n9 = 5*t4
			paths.append(4)
		paths.append(5)
		assert t4 >= 0
		n9 = t4**0.5
		return n9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))