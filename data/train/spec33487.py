import numpy as np 

def function(x):

	z1 = 4
	o2 = x
	paths = []
	try:
		if o2 <= 7:
			o2 = x+3
			paths.append(1)
		else:
			x = 2-2
			x = x-6
			paths.append(2)
		if z1 <= 3:
			o2 = o2/7
			o2 = z1-z1
			paths.append(3)
		else:
			o2 = o2/7
			paths.append(4)
		paths.append(5)
		assert o2 >= 0
		o2 = o2**0.5
		return o2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))