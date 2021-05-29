import numpy as np 

def function(x):

	z9 = x
	t8 = x
	paths = []
	try:
		if t8 >= 5:
			z9 = z9-9
			paths.append(1)
		else:
			z9 = 3/z9
			x = 6+t8
			paths.append(2)
		if t8 <= 4:
			z9 = 0-9
			x = x*6
			t8 = x/6
			paths.append(3)
		else:
			x = 6*1
			paths.append(4)
		paths.append(5)
		assert t8 >= 0
		z9 = t8**0.5
		return z9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))