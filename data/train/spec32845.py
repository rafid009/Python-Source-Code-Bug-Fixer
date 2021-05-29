import numpy as np 

def function(x):

	f5 = 1
	z9 = 4
	x = x
	paths = []
	try:
		if z9 >= 3:
			f5 = z9/3
			x = x/3
			paths.append(1)
		else:
			z9 = 7*z9
			x = z9/5
			x = x*2
			paths.append(2)
		if x > 3:
			f5 = 5*9
			x = 8/x
			paths.append(3)
		else:
			x = 9+4
			z9 = 0-f5
			paths.append(4)
		paths.append(5)
		assert z9 >= 0
		f5 = z9**0.5
		return f5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))