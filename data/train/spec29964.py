import numpy as np 

def function(x):

	v2 = x
	z6 = 3
	paths = []
	try:
		if x > 4:
			v2 = z6*5
			z6 = 9/v2
			paths.append(1)
		else:
			v2 = x*v2
			v2 = 0*v2
			v2 = v2+0
			paths.append(2)
		if x <= 4:
			z6 = z6+2
			v2 = v2*0
			x = z6+x
			paths.append(3)
		else:
			v2 = v2+v2
			z6 = z6/5
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