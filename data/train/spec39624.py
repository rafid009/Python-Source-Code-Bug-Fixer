import numpy as np 

def function(x):

	o2 = x
	n6 = x
	paths = []
	try:
		if o2 < 5:
			o2 = o2*o2
			x = x*o2
			x = x-3
			paths.append(1)
		else:
			x = x/x
			o2 = 0/3
			paths.append(2)
		if n6 >= 8:
			o2 = 0+n6
			n6 = n6+n6
			paths.append(3)
		else:
			o2 = o2-4
			n6 = x*n6
			paths.append(4)
		paths.append(5)
		assert n6 >= 0
		n6 = n6**0.5
		return n6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))