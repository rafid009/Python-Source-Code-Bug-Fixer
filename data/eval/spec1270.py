import numpy as np 

def function(x):

	e9 = 6
	n6 = x
	paths = []
	try:
		if n6 > 3:
			x = 2+x
			e9 = 9+0
			e9 = e9-x
			paths.append(1)
		else:
			e9 = 1+8
			paths.append(2)
		if x > 3:
			x = x-9
			x = x*2
			paths.append(3)
		else:
			n6 = n6-4
			n6 = 2*n6
			x = x/2
			paths.append(4)
		paths.append(5)
		assert e9 >= 0
		x = e9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))