import numpy as np 

def function(x):

	z7 = x
	i6 = 5
	paths = []
	try:
		if x < 8:
			z7 = z7/9
			z7 = 7-z7
			paths.append(1)
		else:
			z7 = x*x
			paths.append(2)
		if i6 <= 5:
			i6 = 9/i6
			i6 = 4-x
			i6 = i6*8
			paths.append(3)
		else:
			x = i6*4
			i6 = x+z7
			x = x+0
			paths.append(4)
		paths.append(5)
		assert i6 >= 0
		x = i6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))