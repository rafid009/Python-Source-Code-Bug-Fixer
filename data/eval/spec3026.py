import numpy as np 

def function(x):

	k9 = x
	z7 = 2
	paths = []
	try:
		if x > 8:
			k9 = 1/k9
			k9 = 6-2
			k9 = 7-6
			paths.append(1)
		else:
			z7 = z7+k9
			k9 = k9+8
			z7 = k9-5
			paths.append(2)
		if x <= 6:
			k9 = 2-k9
			k9 = x/2
			k9 = 7*k9
			paths.append(3)
		else:
			k9 = 9-z7
			z7 = k9-8
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