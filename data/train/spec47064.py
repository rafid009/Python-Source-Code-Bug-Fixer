import numpy as np 

def function(x):

	k9 = x
	a6 = 5
	paths = []
	try:
		if a6 < 0:
			k9 = 2+k9
			k9 = k9+7
			x = 9*x
			paths.append(1)
		else:
			x = x*a6
			x = x-k9
			paths.append(2)
		if x <= 3:
			a6 = a6/4
			a6 = a6-6
			paths.append(3)
		else:
			k9 = 6/k9
			a6 = a6+4
			k9 = 9/k9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a6 = x**0.5
		return a6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))