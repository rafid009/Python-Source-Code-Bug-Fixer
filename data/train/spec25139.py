import numpy as np 

def function(x):

	e6 = x
	k9 = x
	paths = []
	try:
		if x >= 6:
			k9 = k9+x
			k9 = 2-5
			paths.append(1)
		else:
			k9 = 6-k9
			e6 = 5+e6
			paths.append(2)
		if e6 >= 4:
			e6 = e6/2
			paths.append(3)
		else:
			x = e6*x
			k9 = 7-k9
			paths.append(4)
		paths.append(5)
		assert e6 >= 0
		x = e6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))