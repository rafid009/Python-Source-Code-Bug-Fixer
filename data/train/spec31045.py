import numpy as np 

def function(x):

	t3 = 8
	z9 = 2
	paths = []
	try:
		if x < 7:
			t3 = x+z9
			z9 = 6*z9
			z9 = 5/6
			paths.append(1)
		else:
			t3 = t3-4
			z9 = 9-z9
			z9 = 2-z9
			paths.append(2)
		if t3 < 0:
			z9 = 6-9
			t3 = 5+t3
			paths.append(3)
		else:
			x = 7*9
			t3 = x*t3
			x = 4/7
			paths.append(4)
		paths.append(5)
		assert z9 >= 0
		x = z9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))