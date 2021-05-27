import numpy as np 

def function(x):

	k6 = 8
	o7 = 8
	paths = []
	try:
		if o7 >= 6:
			k6 = k6-x
			o7 = k6+x
			paths.append(1)
		else:
			x = 5-x
			paths.append(2)
		if o7 < 3:
			x = o7*x
			k6 = 2/o7
			x = 8/o7
			paths.append(3)
		else:
			o7 = 6/o7
			paths.append(4)
		paths.append(5)
		assert k6 >= 0
		k6 = k6**0.5
		return k6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))