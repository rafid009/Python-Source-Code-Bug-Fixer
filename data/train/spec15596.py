import numpy as np 

def function(x):

	q8 = x
	n2 = 1
	paths = []
	try:
		if q8 >= 0:
			q8 = q8*6
			paths.append(1)
		else:
			q8 = n2+0
			q8 = q8/1
			x = 5/x
			paths.append(2)
		if q8 > 5:
			x = x+9
			q8 = q8/7
			paths.append(3)
		else:
			n2 = n2/8
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