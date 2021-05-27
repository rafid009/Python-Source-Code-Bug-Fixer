import numpy as np 

def function(x):

	a4 = x
	n3 = x
	paths = []
	try:
		if x > 2:
			n3 = 2/1
			n3 = 1/9
			paths.append(1)
		else:
			x = 8/x
			n3 = a4-a4
			a4 = x+5
			paths.append(2)
		if a4 < 4:
			x = 1/x
			n3 = n3+n3
			paths.append(3)
		else:
			a4 = 6/a4
			paths.append(4)
		paths.append(5)
		assert a4 >= 0
		x = a4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))