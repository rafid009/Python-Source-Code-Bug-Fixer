import numpy as np 

def function(x):

	b0 = 9
	k6 = x
	x = 5
	paths = []
	try:
		if k6 > 3:
			b0 = 7*b0
			paths.append(1)
		else:
			x = k6/x
			x = x*5
			paths.append(2)
		if b0 >= 6:
			b0 = 7/x
			b0 = 3*b0
			k6 = k6/6
			paths.append(3)
		else:
			x = b0*x
			x = 0+k6
			x = x-x
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