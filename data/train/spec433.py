import numpy as np 

def function(x):

	i4 = x
	z8 = x
	paths = []
	try:
		if x <= 5:
			i4 = 4+z8
			paths.append(1)
		else:
			z8 = 6+z8
			i4 = i4-z8
			x = x*1
			paths.append(2)
		if x < 7:
			i4 = 6*i4
			paths.append(3)
		else:
			i4 = i4/8
			x = x*3
			i4 = i4+2
			paths.append(4)
		paths.append(5)
		assert z8 >= 0
		i4 = z8**0.5
		return i4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))