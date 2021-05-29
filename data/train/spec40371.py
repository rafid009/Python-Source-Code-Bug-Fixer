import numpy as np 

def function(x):

	z0 = 6
	t7 = 9
	paths = []
	try:
		if t7 <= 9:
			x = x-7
			z0 = 9*1
			t7 = 7+t7
			paths.append(1)
		else:
			x = x/6
			t7 = t7*0
			z0 = 9-z0
			paths.append(2)
		if z0 >= 7:
			z0 = t7*0
			x = z0-t7
			paths.append(3)
		else:
			t7 = x/t7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t7 = x**0.5
		return t7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))