import numpy as np 

def function(x):

	z6 = 9
	f8 = 5
	paths = []
	try:
		if x < 1:
			f8 = f8+2
			paths.append(1)
		else:
			x = 5+x
			z6 = z6-6
			f8 = x*9
			paths.append(2)
		if z6 < 9:
			x = 4*f8
			x = z6+3
			paths.append(3)
		else:
			z6 = z6*9
			z6 = 2+f8
			f8 = f8-z6
			paths.append(4)
		paths.append(5)
		assert f8 >= 0
		f8 = f8**0.5
		return f8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))