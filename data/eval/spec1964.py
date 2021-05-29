import numpy as np 

def function(x):

	n2 = 3
	o2 = x
	x = 4
	paths = []
	try:
		if o2 <= 5:
			n2 = x+9
			n2 = n2*4
			o2 = o2*8
			paths.append(1)
		else:
			o2 = o2-9
			x = 7/8
			x = x-9
			paths.append(2)
		if o2 <= 2:
			x = o2-4
			x = 1/n2
			paths.append(3)
		else:
			n2 = o2*8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o2 = x**0.5
		return o2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))