import numpy as np 

def function(x):

	z7 = 7
	k9 = 3
	paths = []
	try:
		if x < 6:
			z7 = z7/3
			z7 = 9-x
			paths.append(1)
		else:
			k9 = k9-2
			paths.append(2)
		if z7 < 6:
			z7 = z7*5
			k9 = k9/k9
			k9 = 6/z7
			paths.append(3)
		else:
			x = x*1
			k9 = k9/k9
			z7 = z7/x
			paths.append(4)
		paths.append(5)
		assert z7 >= 0
		k9 = z7**0.5
		return k9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))