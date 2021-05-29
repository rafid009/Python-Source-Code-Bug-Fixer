import numpy as np 

def function(x):

	z1 = 9
	v3 = x
	x = x
	paths = []
	try:
		if x >= 9:
			z1 = 1-z1
			z1 = x-z1
			paths.append(1)
		else:
			z1 = 5-0
			v3 = v3*0
			paths.append(2)
		if v3 <= 0:
			z1 = x-9
			v3 = v3+3
			x = 7-6
			paths.append(3)
		else:
			x = 4*6
			v3 = z1*v3
			z1 = 9/9
			paths.append(4)
		paths.append(5)
		assert z1 >= 0
		v3 = z1**0.5
		return v3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))