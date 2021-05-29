import numpy as np 

def function(x):

	o2 = x
	n8 = 9
	paths = []
	try:
		if x >= 2:
			n8 = n8+7
			n8 = n8*n8
			n8 = 7-x
			paths.append(1)
		else:
			x = 6+n8
			o2 = x*x
			o2 = 1*x
			paths.append(2)
		if x <= 0:
			o2 = o2/6
			x = x-n8
			paths.append(3)
		else:
			o2 = 3-o2
			o2 = o2/6
			paths.append(4)
		paths.append(5)
		assert o2 >= 0
		n8 = o2**0.5
		return n8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))