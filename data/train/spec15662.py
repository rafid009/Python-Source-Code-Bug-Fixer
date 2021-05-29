import numpy as np 

def function(x):

	z6 = 5
	v0 = 9
	paths = []
	try:
		if z6 <= 6:
			x = x/7
			z6 = 1-x
			v0 = 0/v0
			paths.append(1)
		else:
			x = x*0
			z6 = z6+5
			paths.append(2)
		if x < 3:
			z6 = v0+z6
			paths.append(3)
		else:
			x = z6+x
			z6 = 2/z6
			paths.append(4)
		paths.append(5)
		assert z6 >= 0
		v0 = z6**0.5
		return v0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))