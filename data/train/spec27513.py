import numpy as np 

def function(x):

	u3 = 5
	z9 = 1
	paths = []
	try:
		if z9 > 1:
			u3 = u3+3
			u3 = z9/u3
			paths.append(1)
		else:
			z9 = u3/u3
			u3 = u3-9
			z9 = z9*5
			paths.append(2)
		if x < 9:
			z9 = 2+3
			u3 = 2/x
			x = 7+8
			paths.append(3)
		else:
			u3 = u3+1
			u3 = 7*u3
			paths.append(4)
		paths.append(5)
		assert u3 >= 0
		z9 = u3**0.5
		return z9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))