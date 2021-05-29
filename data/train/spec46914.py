import numpy as np 

def function(x):

	z4 = 5
	f3 = x
	paths = []
	try:
		if f3 < 2:
			f3 = 1+f3
			paths.append(1)
		else:
			z4 = x-5
			paths.append(2)
		if x <= 0:
			z4 = z4+x
			f3 = 3*f3
			f3 = f3*5
			paths.append(3)
		else:
			x = 7+0
			x = z4+f3
			f3 = 2+3
			paths.append(4)
		paths.append(5)
		assert z4 >= 0
		f3 = z4**0.5
		return f3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))