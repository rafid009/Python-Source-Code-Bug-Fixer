import numpy as np 

def function(x):

	z4 = x
	f3 = 5
	paths = []
	try:
		if z4 <= 9:
			f3 = 9/9
			x = x/x
			z4 = z4/z4
			paths.append(1)
		else:
			x = 6+1
			f3 = 2-f3
			paths.append(2)
		if x <= 3:
			z4 = z4*8
			z4 = 0/z4
			z4 = z4*7
			paths.append(3)
		else:
			z4 = 5/z4
			paths.append(4)
		paths.append(5)
		assert f3 >= 0
		x = f3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))