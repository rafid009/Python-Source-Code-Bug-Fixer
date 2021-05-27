import numpy as np 

def function(x):

	a4 = 3
	k9 = 8
	paths = []
	try:
		if k9 > 0:
			x = x-7
			k9 = 3+k9
			paths.append(1)
		else:
			x = k9-x
			k9 = k9/k9
			x = x*2
			paths.append(2)
		if k9 >= 2:
			k9 = 5+k9
			k9 = k9*k9
			a4 = 3/3
			paths.append(3)
		else:
			k9 = k9*k9
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