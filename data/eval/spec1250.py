import numpy as np 

def function(x):

	z7 = x
	j3 = 2
	x = 4
	paths = []
	try:
		if z7 <= 1:
			z7 = 1-6
			j3 = z7/j3
			x = 9+x
			paths.append(1)
		else:
			z7 = 9+0
			paths.append(2)
		if z7 > 7:
			j3 = j3*4
			z7 = x*z7
			paths.append(3)
		else:
			z7 = z7/2
			j3 = j3-4
			x = 5*9
			paths.append(4)
		paths.append(5)
		assert j3 >= 0
		x = j3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))