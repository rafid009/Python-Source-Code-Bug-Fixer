import numpy as np 

def function(x):

	v2 = 7
	z4 = 9
	paths = []
	try:
		if v2 > 9:
			v2 = z4-1
			z4 = 4-z4
			x = 8*x
			paths.append(1)
		else:
			x = 6/8
			z4 = z4/1
			x = z4+x
			paths.append(2)
		if x > 4:
			z4 = 7+7
			v2 = v2-z4
			paths.append(3)
		else:
			x = 4+z4
			z4 = z4/1
			z4 = x+2
			paths.append(4)
		paths.append(5)
		assert v2 >= 0
		v2 = v2**0.5
		return v2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))