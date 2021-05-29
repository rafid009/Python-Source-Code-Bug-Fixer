import numpy as np 

def function(x):

	o3 = 3
	h2 = x
	x = 8
	paths = []
	try:
		if o3 > 1:
			o3 = o3*h2
			x = o3+x
			paths.append(1)
		else:
			h2 = o3/h2
			paths.append(2)
		if o3 >= 6:
			x = x/x
			paths.append(3)
		else:
			x = h2-6
			x = x/1
			paths.append(4)
		paths.append(5)
		assert h2 >= 0
		o3 = h2**0.5
		return o3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))