import numpy as np 

def function(x):

	r5 = x
	k5 = x
	paths = []
	try:
		if x <= 5:
			k5 = k5-r5
			x = r5/r5
			paths.append(1)
		else:
			r5 = k5+r5
			x = x-6
			r5 = r5-k5
			paths.append(2)
		if r5 >= 0:
			r5 = r5/r5
			k5 = 9-k5
			r5 = 6-7
			paths.append(3)
		else:
			k5 = k5/x
			paths.append(4)
		paths.append(5)
		assert k5 >= 0
		k5 = k5**0.5
		return k5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))