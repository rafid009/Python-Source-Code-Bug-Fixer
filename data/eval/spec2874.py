import numpy as np 

def function(x):

	z2 = 6
	k9 = x
	x = x
	paths = []
	try:
		if z2 >= 2:
			x = 2+x
			x = 9/9
			paths.append(1)
		else:
			x = z2-3
			paths.append(2)
		if x > 9:
			z2 = 1+x
			paths.append(3)
		else:
			z2 = 1-x
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