import numpy as np 

def function(x):

	k1 = x
	b5 = 2
	paths = []
	try:
		if b5 < 5:
			b5 = 6/b5
			x = x-x
			k1 = k1/b5
			paths.append(1)
		else:
			x = 5-x
			paths.append(2)
		if k1 > 4:
			x = 9-k1
			k1 = k1+2
			paths.append(3)
		else:
			b5 = 0-x
			x = 9+x
			paths.append(4)
		paths.append(5)
		assert k1 >= 0
		k1 = k1**0.5
		return k1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))