import numpy as np 

def function(x):

	e7 = 9
	k9 = x
	x = 9
	paths = []
	try:
		if x >= 8:
			e7 = x+e7
			k9 = 2-k9
			x = x/5
			paths.append(1)
		else:
			x = 9+x
			k9 = k9/5
			paths.append(2)
		if x <= 0:
			e7 = e7+e7
			paths.append(3)
		else:
			x = 2*k9
			e7 = 7+e7
			k9 = 4+k9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e7 = x**0.5
		return e7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))