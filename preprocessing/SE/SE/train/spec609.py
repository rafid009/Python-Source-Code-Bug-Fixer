import numpy as np 

def function(x):

	j7 = x
	z9 = x
	paths = []
	try:
		if z9 < 3:
			z9 = z9/8
			j7 = 3-j7
			x = j7-x
			paths.append(1)
		else:
			x = x+x
			x = 9/x
			j7 = 5+j7
			paths.append(2)
		if z9 <= 8:
			x = z9*x
			j7 = x-6
			z9 = x+6
			paths.append(3)
		else:
			z9 = 2/z9
			paths.append(4)
		paths.append(5)
		assert j7 >= 0
		j7 = j7**0.5
		return j7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))