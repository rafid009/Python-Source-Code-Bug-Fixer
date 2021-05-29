import numpy as np 

def function(x):

	d9 = 4
	z9 = 6
	paths = []
	try:
		if x > 2:
			d9 = 0+d9
			d9 = d9-x
			paths.append(1)
		else:
			x = x+8
			paths.append(2)
		if d9 <= 4:
			d9 = x/x
			d9 = 1+4
			z9 = z9/7
			paths.append(3)
		else:
			x = 8*z9
			d9 = d9/1
			d9 = x+7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d9 = x**0.5
		return d9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))