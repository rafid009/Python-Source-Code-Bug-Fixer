import numpy as np 

def function(x):

	z7 = x
	a6 = 7
	paths = []
	try:
		if x < 6:
			x = x*0
			z7 = 9*z7
			a6 = a6+3
			paths.append(1)
		else:
			a6 = a6-3
			z7 = z7-a6
			x = 5/z7
			paths.append(2)
		if a6 <= 9:
			z7 = z7/z7
			a6 = 7+a6
			a6 = a6/a6
			paths.append(3)
		else:
			a6 = a6-7
			paths.append(4)
		paths.append(5)
		assert z7 >= 0
		a6 = z7**0.5
		return a6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))