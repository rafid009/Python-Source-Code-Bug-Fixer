import numpy as np 

def function(x):

	v1 = x
	o2 = x
	paths = []
	try:
		if v1 > 3:
			o2 = o2+x
			paths.append(1)
		else:
			x = 2-v1
			x = 0-4
			paths.append(2)
		if x <= 6:
			v1 = 2/v1
			paths.append(3)
		else:
			x = o2-6
			v1 = v1/7
			paths.append(4)
		paths.append(5)
		assert o2 >= 0
		x = o2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))