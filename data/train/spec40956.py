import numpy as np 

def function(x):

	k9 = x
	d5 = x
	paths = []
	try:
		if d5 < 0:
			x = x+3
			paths.append(1)
		else:
			k9 = 7-0
			x = k9+x
			paths.append(2)
		if d5 >= 9:
			x = 3*3
			paths.append(3)
		else:
			d5 = x-d5
			k9 = d5*k9
			k9 = k9+k9
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