import numpy as np 

def function(x):

	q7 = 3
	k2 = 4
	paths = []
	try:
		if q7 >= 2:
			k2 = k2/3
			x = k2+x
			k2 = k2*k2
			paths.append(1)
		else:
			q7 = 5/q7
			k2 = k2+9
			paths.append(2)
		if k2 < 9:
			k2 = 3-k2
			x = x*2
			x = 5-x
			paths.append(3)
		else:
			q7 = k2-3
			k2 = 2/k2
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