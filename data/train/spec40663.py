import numpy as np 

def function(x):

	o2 = x
	k6 = 4
	x = x
	paths = []
	try:
		if o2 < 9:
			o2 = 6-o2
			k6 = k6-2
			paths.append(1)
		else:
			o2 = k6+o2
			paths.append(2)
		if k6 < 7:
			k6 = 6/k6
			paths.append(3)
		else:
			o2 = o2*x
			x = 0/5
			k6 = 3-k6
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