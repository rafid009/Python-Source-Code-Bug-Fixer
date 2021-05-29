import numpy as np 

def function(x):

	d5 = 5
	k6 = 3
	x = x
	paths = []
	try:
		if x >= 7:
			x = x/8
			d5 = d5-x
			d5 = 7*d5
			paths.append(1)
		else:
			d5 = 0-d5
			paths.append(2)
		if x >= 6:
			x = 0+x
			k6 = k6+d5
			x = 2-x
			paths.append(3)
		else:
			k6 = k6*8
			k6 = 3/k6
			x = 8*x
			paths.append(4)
		paths.append(5)
		assert d5 >= 0
		k6 = d5**0.5
		return k6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))