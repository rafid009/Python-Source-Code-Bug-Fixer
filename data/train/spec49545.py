import numpy as np 

def function(x):

	z9 = 2
	b4 = x
	paths = []
	try:
		if x > 2:
			x = x*2
			z9 = x-8
			b4 = z9/b4
			paths.append(1)
		else:
			z9 = 5+3
			b4 = b4/7
			z9 = x+2
			paths.append(2)
		if x >= 9:
			b4 = 1*9
			paths.append(3)
		else:
			x = x*9
			x = x+1
			z9 = 3+z9
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