import numpy as np 

def function(x):

	k2 = x
	a5 = 0
	x = x
	paths = []
	try:
		if a5 <= 2:
			x = x*4
			a5 = a5-k2
			x = 9*4
			paths.append(1)
		else:
			a5 = 2+k2
			paths.append(2)
		if a5 <= 8:
			a5 = k2-7
			a5 = a5-6
			paths.append(3)
		else:
			x = x*6
			k2 = k2-0
			a5 = 5+a5
			paths.append(4)
		paths.append(5)
		assert k2 >= 0
		x = k2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))