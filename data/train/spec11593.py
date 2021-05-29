import numpy as np 

def function(x):

	d5 = x
	k6 = x
	paths = []
	try:
		if x < 6:
			k6 = k6+k6
			paths.append(1)
		else:
			d5 = x/5
			d5 = 7-d5
			paths.append(2)
		if k6 <= 2:
			x = 9-k6
			paths.append(3)
		else:
			x = x-4
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