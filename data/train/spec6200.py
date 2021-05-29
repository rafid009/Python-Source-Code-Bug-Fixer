import numpy as np 

def function(x):

	k5 = x
	o2 = x
	paths = []
	try:
		if k5 <= 6:
			k5 = o2/x
			x = 9*3
			x = 1+6
			paths.append(1)
		else:
			x = x-3
			paths.append(2)
		if x >= 3:
			o2 = o2*9
			x = 2*1
			x = o2*2
			paths.append(3)
		else:
			k5 = k5-7
			x = o2+2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k5 = x**0.5
		return k5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))