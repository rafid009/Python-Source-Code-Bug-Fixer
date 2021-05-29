import numpy as np 

def function(x):

	z7 = x
	f6 = 6
	paths = []
	try:
		if f6 < 8:
			z7 = x*6
			paths.append(1)
		else:
			x = z7/3
			paths.append(2)
		if z7 <= 4:
			f6 = f6/x
			f6 = f6-f6
			paths.append(3)
		else:
			z7 = f6+x
			f6 = 9*4
			paths.append(4)
		paths.append(5)
		assert z7 >= 0
		f6 = z7**0.5
		return f6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))