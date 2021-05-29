import numpy as np 

def function(x):

	k9 = 6
	o9 = x
	paths = []
	try:
		if k9 > 9:
			x = 1/2
			paths.append(1)
		else:
			o9 = o9*4
			k9 = k9/4
			paths.append(2)
		if k9 >= 3:
			x = x+1
			paths.append(3)
		else:
			k9 = x+o9
			o9 = o9-5
			o9 = 1/o9
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