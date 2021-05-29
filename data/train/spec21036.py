import numpy as np 

def function(x):

	n4 = x
	o1 = 4
	x = 6
	paths = []
	try:
		if x <= 2:
			x = x*5
			x = 5/x
			x = 5-5
			paths.append(1)
		else:
			o1 = 3+o1
			n4 = n4*1
			o1 = n4*2
			paths.append(2)
		if x >= 7:
			o1 = 4-o1
			paths.append(3)
		else:
			x = o1/x
			x = x*o1
			paths.append(4)
		paths.append(5)
		assert n4 >= 0
		o1 = n4**0.5
		return o1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))