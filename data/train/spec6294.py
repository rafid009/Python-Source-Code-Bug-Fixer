import numpy as np 

def function(x):

	e2 = 5
	k9 = 8
	paths = []
	try:
		if x < 6:
			k9 = x/4
			e2 = e2/9
			paths.append(1)
		else:
			e2 = e2-k9
			paths.append(2)
		if e2 < 6:
			k9 = k9-2
			k9 = k9+3
			x = x/8
			paths.append(3)
		else:
			k9 = x-k9
			paths.append(4)
		paths.append(5)
		assert e2 >= 0
		k9 = e2**0.5
		return k9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))