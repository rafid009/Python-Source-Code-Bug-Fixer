import numpy as np 

def function(x):

	z6 = x
	k9 = x
	paths = []
	try:
		if z6 >= 2:
			k9 = 6-k9
			paths.append(1)
		else:
			x = x/6
			x = x*4
			k9 = 2-x
			paths.append(2)
		if k9 <= 4:
			z6 = 9-z6
			x = 1*2
			paths.append(3)
		else:
			x = x+6
			k9 = 9/3
			z6 = z6/4
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