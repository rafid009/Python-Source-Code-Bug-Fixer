import numpy as np 

def function(x):

	v7 = x
	z0 = 2
	x = 9
	paths = []
	try:
		if x <= 0:
			z0 = v7/4
			z0 = z0+9
			paths.append(1)
		else:
			v7 = v7*3
			paths.append(2)
		if x <= 0:
			x = v7/8
			paths.append(3)
		else:
			x = 1+7
			x = x*0
			v7 = v7-9
			paths.append(4)
		paths.append(5)
		assert v7 >= 0
		v7 = v7**0.5
		return v7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))