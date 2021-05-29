import numpy as np 

def function(x):

	l9 = x
	z4 = 6
	x = x
	paths = []
	try:
		if x < 4:
			l9 = x-0
			z4 = z4*l9
			x = 2+x
			paths.append(1)
		else:
			z4 = 6+z4
			l9 = l9-8
			paths.append(2)
		if z4 <= 0:
			l9 = l9/9
			z4 = 8+z4
			paths.append(3)
		else:
			z4 = z4*0
			x = x/2
			paths.append(4)
		paths.append(5)
		assert l9 >= 0
		x = l9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))