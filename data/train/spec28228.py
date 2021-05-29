import numpy as np 

def function(x):

	k2 = 7
	v2 = 4
	paths = []
	try:
		if k2 <= 3:
			x = 5/x
			paths.append(1)
		else:
			k2 = k2+k2
			k2 = x/k2
			x = x+k2
			paths.append(2)
		if x > 5:
			x = k2*x
			paths.append(3)
		else:
			k2 = v2/k2
			x = x*v2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v2 = x**0.5
		return v2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))