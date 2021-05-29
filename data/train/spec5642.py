import numpy as np 

def function(x):

	t5 = 1
	z1 = 3
	paths = []
	try:
		if x <= 1:
			t5 = t5*4
			paths.append(1)
		else:
			x = z1*x
			z1 = 3+1
			paths.append(2)
		if x >= 5:
			x = 1/t5
			z1 = 1/3
			paths.append(3)
		else:
			t5 = 9/x
			t5 = t5-8
			x = 2-x
			paths.append(4)
		paths.append(5)
		assert t5 >= 0
		z1 = t5**0.5
		return z1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))