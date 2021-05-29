import numpy as np 

def function(x):

	z2 = 4
	k9 = 1
	paths = []
	try:
		if k9 < 7:
			z2 = z2-k9
			z2 = 6-0
			z2 = z2-4
			paths.append(1)
		else:
			z2 = x-z2
			paths.append(2)
		if x >= 7:
			z2 = z2-z2
			k9 = 7*k9
			k9 = 5-7
			paths.append(3)
		else:
			k9 = k9-7
			z2 = z2/1
			paths.append(4)
		paths.append(5)
		assert k9 >= 0
		k9 = k9**0.5
		return k9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))