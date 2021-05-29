import numpy as np 

def function(x):

	z2 = 5
	f2 = 6
	paths = []
	try:
		if f2 > 9:
			z2 = 5+6
			f2 = f2*3
			paths.append(1)
		else:
			f2 = 4+0
			f2 = 2+3
			paths.append(2)
		if f2 >= 0:
			x = 5*x
			z2 = z2/7
			z2 = z2-x
			paths.append(3)
		else:
			f2 = f2+2
			paths.append(4)
		paths.append(5)
		assert z2 >= 0
		f2 = z2**0.5
		return f2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))