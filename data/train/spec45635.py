import numpy as np 

def function(x):

	k2 = x
	x7 = x
	paths = []
	try:
		if x < 3:
			x = 9+x
			x = x/k2
			paths.append(1)
		else:
			x = 8-4
			x7 = x7/9
			paths.append(2)
		if k2 <= 0:
			x = x-x
			x = x*8
			paths.append(3)
		else:
			k2 = 4/k2
			x = x+1
			x7 = k2*2
			paths.append(4)
		paths.append(5)
		assert x7 >= 0
		x7 = x7**0.5
		return x7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))