import numpy as np 

def function(x):

	d6 = x
	z2 = x
	paths = []
	try:
		if d6 < 3:
			d6 = 4/x
			d6 = 6+1
			paths.append(1)
		else:
			z2 = z2-z2
			x = 4/x
			d6 = 7-d6
			paths.append(2)
		if x < 5:
			x = 0+x
			x = x*7
			paths.append(3)
		else:
			z2 = x+d6
			z2 = z2+7
			x = 0-4
			paths.append(4)
		paths.append(5)
		assert z2 >= 0
		z2 = z2**0.5
		return z2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))