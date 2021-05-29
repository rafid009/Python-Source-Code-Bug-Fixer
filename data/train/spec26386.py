import numpy as np 

def function(x):

	a3 = x
	k9 = 1
	paths = []
	try:
		if x < 3:
			x = 6/x
			paths.append(1)
		else:
			a3 = a3/a3
			a3 = a3-3
			k9 = k9+a3
			paths.append(2)
		if k9 < 6:
			a3 = 0-7
			a3 = a3-6
			paths.append(3)
		else:
			k9 = k9*9
			k9 = 3-x
			k9 = x*k9
			paths.append(4)
		paths.append(5)
		assert k9 >= 0
		a3 = k9**0.5
		return a3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))