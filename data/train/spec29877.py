import numpy as np 

def function(x):

	l1 = x
	z6 = 8
	paths = []
	try:
		if l1 <= 8:
			z6 = z6-5
			paths.append(1)
		else:
			z6 = z6-7
			l1 = 8/z6
			paths.append(2)
		if x < 6:
			z6 = 5*z6
			paths.append(3)
		else:
			x = z6+5
			l1 = l1/9
			z6 = 8+3
			paths.append(4)
		paths.append(5)
		assert l1 >= 0
		l1 = l1**0.5
		return l1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))