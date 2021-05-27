import numpy as np 

def function(x):

	j2 = x
	z1 = 2
	x = 7
	paths = []
	try:
		if z1 > 0:
			x = x+2
			paths.append(1)
		else:
			z1 = j2-5
			z1 = j2-5
			paths.append(2)
		if x < 8:
			x = j2-z1
			paths.append(3)
		else:
			j2 = 7*j2
			z1 = x+j2
			z1 = z1*z1
			paths.append(4)
		paths.append(5)
		assert j2 >= 0
		j2 = j2**0.5
		return j2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))