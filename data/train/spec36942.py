import numpy as np 

def function(x):

	i2 = x
	z7 = 0
	paths = []
	try:
		if x >= 4:
			i2 = 4+z7
			x = x/3
			i2 = i2*4
			paths.append(1)
		else:
			x = z7+x
			paths.append(2)
		if z7 >= 0:
			x = x*1
			paths.append(3)
		else:
			i2 = i2-8
			z7 = 0+z7
			z7 = 3-5
			paths.append(4)
		paths.append(5)
		assert i2 >= 0
		i2 = i2**0.5
		return i2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))