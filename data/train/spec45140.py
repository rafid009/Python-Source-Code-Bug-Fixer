import numpy as np 

def function(x):

	i3 = 8
	z1 = x
	paths = []
	try:
		if z1 > 4:
			x = 1*x
			z1 = 8-z1
			paths.append(1)
		else:
			i3 = 5*z1
			i3 = z1*3
			i3 = i3+i3
			paths.append(2)
		if x > 1:
			x = 8+x
			z1 = i3-i3
			x = 5+2
			paths.append(3)
		else:
			i3 = i3+z1
			z1 = 9/z1
			paths.append(4)
		paths.append(5)
		assert i3 >= 0
		i3 = i3**0.5
		return i3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))