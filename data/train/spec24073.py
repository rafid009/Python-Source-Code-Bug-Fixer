import numpy as np 

def function(x):

	k1 = x
	r5 = 9
	paths = []
	try:
		if r5 < 7:
			x = x*x
			k1 = k1+6
			paths.append(1)
		else:
			k1 = k1-r5
			k1 = k1+1
			paths.append(2)
		if r5 <= 4:
			k1 = 0-x
			paths.append(3)
		else:
			x = 6/x
			x = x-3
			paths.append(4)
		paths.append(5)
		assert k1 >= 0
		r5 = k1**0.5
		return r5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))