import numpy as np 

def function(x):

	o3 = x
	k9 = 4
	paths = []
	try:
		if k9 >= 9:
			k9 = k9+7
			x = x/x
			x = x/9
			paths.append(1)
		else:
			k9 = k9-k9
			x = 8*o3
			x = x+8
			paths.append(2)
		if k9 > 2:
			x = x*x
			paths.append(3)
		else:
			k9 = x/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k9 = x**0.5
		return k9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))