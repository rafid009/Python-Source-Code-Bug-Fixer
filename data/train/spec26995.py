import numpy as np 

def function(x):

	k2 = x
	r9 = x
	x = x
	paths = []
	try:
		if x > 0:
			k2 = 9/k2
			paths.append(1)
		else:
			x = 0-0
			x = 6-x
			paths.append(2)
		if r9 < 5:
			r9 = r9+7
			x = 1+x
			x = 9+k2
			paths.append(3)
		else:
			k2 = 1*k2
			paths.append(4)
		paths.append(5)
		assert k2 >= 0
		k2 = k2**0.5
		return k2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))