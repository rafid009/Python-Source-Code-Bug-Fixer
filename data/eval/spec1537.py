import numpy as np 

def function(x):

	f7 = 5
	z4 = x
	paths = []
	try:
		if z4 < 5:
			f7 = f7-1
			x = f7/1
			paths.append(1)
		else:
			f7 = f7/f7
			x = 3+x
			z4 = 7+f7
			paths.append(2)
		if x <= 5:
			x = 0/z4
			f7 = 2/f7
			f7 = f7-4
			paths.append(3)
		else:
			f7 = f7/2
			f7 = f7-1
			z4 = f7-4
			paths.append(4)
		paths.append(5)
		assert f7 >= 0
		f7 = f7**0.5
		return f7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))