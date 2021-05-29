import numpy as np 

def function(x):

	z2 = x
	j6 = x
	paths = []
	try:
		if j6 <= 6:
			x = x+1
			paths.append(1)
		else:
			j6 = 3-j6
			paths.append(2)
		if z2 >= 4:
			j6 = j6+4
			z2 = 6*5
			j6 = 7+9
			paths.append(3)
		else:
			j6 = 7-j6
			j6 = x*4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))