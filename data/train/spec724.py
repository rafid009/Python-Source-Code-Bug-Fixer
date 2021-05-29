import numpy as np 

def function(x):

	z9 = x
	k3 = x
	x = 4
	paths = []
	try:
		if x <= 8:
			x = x*1
			z9 = z9-6
			x = x*z9
			paths.append(1)
		else:
			x = 4/2
			k3 = k3/5
			paths.append(2)
		if x > 2:
			x = x+z9
			k3 = 5*x
			z9 = z9-z9
			paths.append(3)
		else:
			k3 = k3-5
			x = 2*1
			x = 0+x
			paths.append(4)
		paths.append(5)
		assert k3 >= 0
		z9 = k3**0.5
		return z9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))