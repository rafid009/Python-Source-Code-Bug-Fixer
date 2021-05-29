import numpy as np 

def function(x):

	n0 = x
	k6 = 0
	paths = []
	try:
		if x < 9:
			x = x+n0
			n0 = n0/5
			x = x/7
			paths.append(1)
		else:
			k6 = k6/2
			paths.append(2)
		if k6 >= 4:
			n0 = 2-n0
			n0 = n0*5
			k6 = 4/k6
			paths.append(3)
		else:
			k6 = k6+5
			n0 = x/9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))