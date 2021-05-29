import numpy as np 

def function(x):

	z5 = x
	u3 = x
	paths = []
	try:
		if x < 3:
			z5 = 5*z5
			u3 = 5-6
			paths.append(1)
		else:
			u3 = x+3
			u3 = 3-u3
			z5 = z5/4
			paths.append(2)
		if x > 4:
			u3 = x/z5
			paths.append(3)
		else:
			x = x*1
			x = u3/8
			x = 6-x
			paths.append(4)
		paths.append(5)
		assert u3 >= 0
		x = u3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))