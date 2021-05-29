import numpy as np 

def function(x):

	v2 = x
	d7 = x
	paths = []
	try:
		if d7 > 4:
			d7 = 4*d7
			paths.append(1)
		else:
			d7 = d7-5
			x = 7*d7
			v2 = x-v2
			paths.append(2)
		if x >= 0:
			v2 = v2-x
			paths.append(3)
		else:
			x = d7/1
			v2 = 2*v2
			x = 9*x
			paths.append(4)
		paths.append(5)
		assert v2 >= 0
		x = v2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))