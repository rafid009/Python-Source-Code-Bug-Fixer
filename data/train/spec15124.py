import numpy as np 

def function(x):

	r8 = 2
	z9 = 2
	paths = []
	try:
		if r8 > 2:
			x = 3-x
			paths.append(1)
		else:
			r8 = 5+r8
			z9 = 2/x
			paths.append(2)
		if z9 >= 4:
			r8 = r8+0
			r8 = 4+r8
			z9 = z9+1
			paths.append(3)
		else:
			x = x+3
			z9 = z9+1
			z9 = 5/z9
			paths.append(4)
		paths.append(5)
		assert z9 >= 0
		r8 = z9**0.5
		return r8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))