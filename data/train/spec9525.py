import numpy as np 

def function(x):

	e8 = x
	k9 = 3
	paths = []
	try:
		if e8 <= 7:
			k9 = k9*9
			paths.append(1)
		else:
			k9 = k9-5
			k9 = 8/k9
			paths.append(2)
		if x <= 7:
			e8 = 1*6
			k9 = k9+4
			paths.append(3)
		else:
			e8 = x*e8
			k9 = k9-8
			x = x+1
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