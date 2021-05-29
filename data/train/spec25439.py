import numpy as np 

def function(x):

	z4 = x
	j9 = x
	paths = []
	try:
		if x >= 0:
			j9 = j9/4
			j9 = j9*5
			z4 = 6+z4
			paths.append(1)
		else:
			x = x+8
			paths.append(2)
		if j9 > 0:
			x = x+8
			z4 = z4+x
			j9 = 7*j9
			paths.append(3)
		else:
			j9 = j9/z4
			paths.append(4)
		paths.append(5)
		assert z4 >= 0
		j9 = z4**0.5
		return j9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))