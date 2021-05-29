import numpy as np 

def function(x):

	z2 = x
	j3 = 8
	paths = []
	try:
		if z2 > 1:
			j3 = 4-6
			paths.append(1)
		else:
			j3 = 5-j3
			j3 = 2-z2
			paths.append(2)
		if z2 <= 6:
			z2 = j3-8
			paths.append(3)
		else:
			j3 = j3-6
			z2 = 3/z2
			x = x/2
			paths.append(4)
		paths.append(5)
		assert z2 >= 0
		j3 = z2**0.5
		return j3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))