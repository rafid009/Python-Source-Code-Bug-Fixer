import numpy as np 

def function(x):

	k2 = 4
	b9 = 0
	paths = []
	try:
		if k2 <= 9:
			b9 = b9+7
			paths.append(1)
		else:
			b9 = b9+x
			x = x+6
			k2 = 7/4
			paths.append(2)
		if x > 1:
			x = 8-0
			b9 = 0-b9
			x = x-b9
			paths.append(3)
		else:
			k2 = k2+x
			x = 2/k2
			paths.append(4)
		paths.append(5)
		assert k2 >= 0
		b9 = k2**0.5
		return b9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))