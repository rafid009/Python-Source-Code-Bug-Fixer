import numpy as np 

def function(x):

	o4 = x
	n3 = 4
	x = x
	paths = []
	try:
		if n3 < 4:
			o4 = 7-o4
			x = o4*o4
			paths.append(1)
		else:
			n3 = 2-5
			o4 = 0+o4
			o4 = o4*1
			paths.append(2)
		if o4 >= 9:
			n3 = 3-5
			x = x-4
			x = 7*x
			paths.append(3)
		else:
			x = o4/3
			paths.append(4)
		paths.append(5)
		assert o4 >= 0
		n3 = o4**0.5
		return n3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))