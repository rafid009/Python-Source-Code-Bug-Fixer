import numpy as np 

def function(x):

	z1 = 5
	b4 = x
	paths = []
	try:
		if b4 > 7:
			x = 1+x
			x = x*8
			paths.append(1)
		else:
			b4 = 9*b4
			b4 = b4*z1
			x = b4*b4
			paths.append(2)
		if z1 > 9:
			z1 = 1/8
			b4 = 0*b4
			paths.append(3)
		else:
			z1 = z1*b4
			x = x+x
			x = x*b4
			paths.append(4)
		paths.append(5)
		assert z1 >= 0
		b4 = z1**0.5
		return b4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))