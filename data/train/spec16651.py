import numpy as np 

def function(x):

	o7 = 8
	k5 = x
	paths = []
	try:
		if k5 < 9:
			o7 = 5+k5
			paths.append(1)
		else:
			k5 = 1+8
			k5 = 2+k5
			paths.append(2)
		if x >= 8:
			x = 0+x
			x = x*8
			paths.append(3)
		else:
			o7 = 4*5
			k5 = 3*k5
			paths.append(4)
		paths.append(5)
		assert k5 >= 0
		k5 = k5**0.5
		return k5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))