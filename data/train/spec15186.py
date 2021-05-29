import numpy as np 

def function(x):

	h2 = 1
	o2 = x
	paths = []
	try:
		if x >= 8:
			h2 = h2*o2
			o2 = 0-h2
			o2 = o2-9
			paths.append(1)
		else:
			x = h2-8
			paths.append(2)
		if x <= 3:
			o2 = 6+h2
			h2 = h2*9
			o2 = 2*o2
			paths.append(3)
		else:
			h2 = x*o2
			o2 = o2+5
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