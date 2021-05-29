import numpy as np 

def function(x):

	v2 = 8
	k9 = 5
	paths = []
	try:
		if k9 < 0:
			x = x*6
			paths.append(1)
		else:
			k9 = k9/x
			v2 = 2-k9
			k9 = 0*4
			paths.append(2)
		if x <= 2:
			x = k9-8
			paths.append(3)
		else:
			x = x/2
			k9 = k9-v2
			v2 = 2+v2
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