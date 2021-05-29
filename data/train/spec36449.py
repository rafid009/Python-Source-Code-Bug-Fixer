import numpy as np 

def function(x):

	b4 = 8
	z9 = 2
	paths = []
	try:
		if b4 < 9:
			z9 = 3-7
			paths.append(1)
		else:
			b4 = 3*5
			b4 = b4*6
			paths.append(2)
		if x > 6:
			b4 = x*2
			paths.append(3)
		else:
			z9 = 5/3
			paths.append(4)
		paths.append(5)
		assert z9 >= 0
		z9 = z9**0.5
		return z9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))