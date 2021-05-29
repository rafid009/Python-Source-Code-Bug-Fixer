import numpy as np 

def function(x):

	k7 = x
	e0 = x
	paths = []
	try:
		if e0 <= 1:
			k7 = 9*k7
			x = x*8
			paths.append(1)
		else:
			x = 4*9
			e0 = 4+0
			k7 = 2/k7
			paths.append(2)
		if x <= 9:
			x = x-6
			x = 0+3
			paths.append(3)
		else:
			e0 = 6-e0
			x = x/5
			paths.append(4)
		paths.append(5)
		assert e0 >= 0
		x = e0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))