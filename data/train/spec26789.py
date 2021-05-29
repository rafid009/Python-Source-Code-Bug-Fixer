import numpy as np 

def function(x):

	u3 = x
	z1 = 6
	paths = []
	try:
		if u3 < 3:
			u3 = u3/9
			x = 0*5
			z1 = z1-x
			paths.append(1)
		else:
			u3 = 5-z1
			x = x+9
			paths.append(2)
		if x > 5:
			x = u3*x
			x = 0+4
			paths.append(3)
		else:
			u3 = 2*u3
			u3 = u3/u3
			u3 = u3/5
			paths.append(4)
		paths.append(5)
		assert u3 >= 0
		z1 = u3**0.5
		return z1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))