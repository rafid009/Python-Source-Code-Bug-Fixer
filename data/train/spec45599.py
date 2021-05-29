import numpy as np 

def function(x):

	i3 = 5
	z1 = x
	x = 8
	paths = []
	try:
		if z1 <= 8:
			x = x*2
			x = x*z1
			x = x+i3
			paths.append(1)
		else:
			z1 = 5*z1
			z1 = 7*z1
			z1 = 7*z1
			paths.append(2)
		if x >= 1:
			i3 = 8/i3
			paths.append(3)
		else:
			x = i3+4
			i3 = x+x
			i3 = z1/i3
			paths.append(4)
		paths.append(5)
		assert z1 >= 0
		x = z1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))