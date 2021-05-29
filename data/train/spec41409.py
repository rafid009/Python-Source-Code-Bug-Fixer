import numpy as np 

def function(x):

	r8 = 6
	z1 = 0
	paths = []
	try:
		if x >= 8:
			r8 = r8+1
			z1 = x+6
			paths.append(1)
		else:
			r8 = 9/4
			z1 = z1+1
			paths.append(2)
		if r8 <= 4:
			z1 = 4/x
			paths.append(3)
		else:
			x = x-x
			r8 = 4*8
			z1 = x*x
			paths.append(4)
		paths.append(5)
		assert z1 >= 0
		x = z1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))