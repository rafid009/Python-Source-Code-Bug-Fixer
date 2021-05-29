import numpy as np 

def function(x):

	q0 = 4
	z9 = 1
	paths = []
	try:
		if q0 > 7:
			x = x+3
			x = 8/x
			paths.append(1)
		else:
			q0 = q0-7
			z9 = x/z9
			paths.append(2)
		if x > 2:
			z9 = z9*9
			x = x+7
			paths.append(3)
		else:
			q0 = q0+x
			z9 = 8/7
			z9 = 6*0
			paths.append(4)
		paths.append(5)
		assert q0 >= 0
		x = q0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))