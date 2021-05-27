import numpy as np 

def function(x):

	z4 = 3
	t4 = x
	paths = []
	try:
		if x < 5:
			x = x*8
			z4 = 4/4
			z4 = x-z4
			paths.append(1)
		else:
			z4 = x*8
			x = x+5
			paths.append(2)
		if x >= 1:
			t4 = 7+2
			x = 2-x
			z4 = 3/t4
			paths.append(3)
		else:
			t4 = t4*9
			x = 5*8
			paths.append(4)
		paths.append(5)
		assert z4 >= 0
		t4 = z4**0.5
		return t4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))