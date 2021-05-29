import numpy as np 

def function(x):

	z6 = x
	f8 = 9
	x = 1
	paths = []
	try:
		if f8 >= 4:
			z6 = 7/z6
			x = 3*8
			z6 = 9/z6
			paths.append(1)
		else:
			x = z6*z6
			paths.append(2)
		if f8 <= 9:
			f8 = f8+f8
			paths.append(3)
		else:
			f8 = 5-f8
			x = x/8
			f8 = x*9
			paths.append(4)
		paths.append(5)
		assert z6 >= 0
		f8 = z6**0.5
		return f8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))