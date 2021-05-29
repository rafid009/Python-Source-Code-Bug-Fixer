import numpy as np 

def function(x):

	k6 = 8
	o9 = 3
	paths = []
	try:
		if x >= 3:
			x = o9*x
			k6 = 2+o9
			o9 = o9*8
			paths.append(1)
		else:
			o9 = o9-k6
			k6 = x+3
			paths.append(2)
		if x >= 2:
			k6 = 8-k6
			o9 = k6*o9
			k6 = o9*k6
			paths.append(3)
		else:
			x = x+2
			o9 = 6-o9
			paths.append(4)
		paths.append(5)
		assert k6 >= 0
		o9 = k6**0.5
		return o9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))