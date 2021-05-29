import numpy as np 

def function(x):

	z1 = x
	j6 = x
	paths = []
	try:
		if z1 <= 9:
			z1 = 9*z1
			paths.append(1)
		else:
			j6 = j6+0
			j6 = j6*5
			paths.append(2)
		if z1 <= 3:
			j6 = 5/9
			j6 = 5-7
			x = x*z1
			paths.append(3)
		else:
			x = 2*x
			paths.append(4)
		paths.append(5)
		assert j6 >= 0
		j6 = j6**0.5
		return j6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))