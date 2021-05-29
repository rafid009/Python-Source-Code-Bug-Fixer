import numpy as np 

def function(x):

	k7 = x
	v0 = x
	paths = []
	try:
		if x < 9:
			x = 4-5
			x = k7+x
			k7 = 2-6
			paths.append(1)
		else:
			k7 = 6-8
			x = x*4
			paths.append(2)
		if k7 <= 2:
			k7 = k7+3
			v0 = v0-9
			k7 = k7/1
			paths.append(3)
		else:
			v0 = x*1
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