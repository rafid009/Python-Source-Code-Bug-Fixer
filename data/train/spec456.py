import numpy as np 

def function(x):

	b5 = x
	z4 = x
	paths = []
	try:
		if x < 3:
			x = x+x
			x = x*4
			paths.append(1)
		else:
			b5 = b5/6
			x = x-5
			x = x*x
			paths.append(2)
		if z4 <= 4:
			z4 = b5/x
			paths.append(3)
		else:
			z4 = z4+6
			x = x/9
			paths.append(4)
		paths.append(5)
		assert b5 >= 0
		x = b5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))