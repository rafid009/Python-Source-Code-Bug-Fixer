import numpy as np 

def function(x):

	k9 = 6
	e5 = 2
	paths = []
	try:
		if k9 < 9:
			e5 = 9-k9
			k9 = k9/8
			paths.append(1)
		else:
			x = 0+e5
			paths.append(2)
		if k9 < 4:
			k9 = 8+8
			paths.append(3)
		else:
			x = 6/x
			k9 = 6/9
			k9 = x+5
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