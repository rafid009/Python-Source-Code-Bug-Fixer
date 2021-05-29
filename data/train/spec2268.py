import numpy as np 

def function(x):

	b8 = 1
	k9 = 6
	paths = []
	try:
		if x > 7:
			b8 = 6/6
			paths.append(1)
		else:
			k9 = k9-1
			paths.append(2)
		if k9 >= 2:
			b8 = 5-0
			x = x*5
			b8 = b8/b8
			paths.append(3)
		else:
			k9 = k9+6
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