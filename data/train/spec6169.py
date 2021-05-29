import numpy as np 

def function(x):

	z9 = x
	e4 = x
	paths = []
	try:
		if e4 >= 9:
			z9 = z9*3
			e4 = e4-3
			z9 = z9/1
			paths.append(1)
		else:
			e4 = e4*0
			paths.append(2)
		if z9 <= 4:
			e4 = 5-0
			e4 = e4-6
			z9 = x-z9
			paths.append(3)
		else:
			z9 = 2-1
			x = x/x
			z9 = z9*8
			paths.append(4)
		paths.append(5)
		assert e4 >= 0
		e4 = e4**0.5
		return e4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))