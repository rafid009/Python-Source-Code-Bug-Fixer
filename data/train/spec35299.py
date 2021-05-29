import numpy as np 

def function(x):

	o0 = x
	z9 = 6
	paths = []
	try:
		if o0 < 8:
			z9 = z9-2
			z9 = z9*z9
			z9 = o0-6
			paths.append(1)
		else:
			z9 = 8+z9
			z9 = x/9
			paths.append(2)
		if o0 <= 0:
			o0 = o0+1
			o0 = 7*o0
			paths.append(3)
		else:
			o0 = 2-5
			x = x+1
			paths.append(4)
		paths.append(5)
		assert z9 >= 0
		o0 = z9**0.5
		return o0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))