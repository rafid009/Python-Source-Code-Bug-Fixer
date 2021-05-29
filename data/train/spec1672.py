import numpy as np 

def function(x):

	z2 = 7
	f5 = 0
	paths = []
	try:
		if f5 >= 4:
			z2 = z2/z2
			paths.append(1)
		else:
			z2 = z2-3
			paths.append(2)
		if z2 < 7:
			f5 = f5+f5
			z2 = 6+x
			f5 = 8-z2
			paths.append(3)
		else:
			z2 = x*9
			f5 = f5/8
			x = 6-x
			paths.append(4)
		paths.append(5)
		assert z2 >= 0
		f5 = z2**0.5
		return f5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))