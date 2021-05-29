import numpy as np 

def function(x):

	o2 = 3
	k6 = 2
	paths = []
	try:
		if x > 6:
			k6 = k6-2
			paths.append(1)
		else:
			k6 = 9-2
			k6 = 5-k6
			o2 = 7*o2
			paths.append(2)
		if k6 <= 6:
			o2 = 3-5
			x = k6/o2
			paths.append(3)
		else:
			o2 = 7*o2
			o2 = k6-o2
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