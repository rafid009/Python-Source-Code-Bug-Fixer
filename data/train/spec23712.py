import numpy as np 

def function(x):

	v0 = 5
	k7 = 6
	paths = []
	try:
		if k7 >= 8:
			x = x/k7
			k7 = 1+k7
			paths.append(1)
		else:
			x = k7-x
			x = x+0
			k7 = 5-k7
			paths.append(2)
		if v0 <= 9:
			v0 = v0*x
			k7 = 8-k7
			paths.append(3)
		else:
			v0 = x/v0
			k7 = k7*9
			v0 = v0-8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k7 = x**0.5
		return k7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))