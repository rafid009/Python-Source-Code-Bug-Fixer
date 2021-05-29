import numpy as np 

def function(x):

	t4 = x
	z6 = x
	paths = []
	try:
		if t4 <= 3:
			t4 = t4*7
			t4 = 1-9
			paths.append(1)
		else:
			x = x*z6
			t4 = t4/9
			paths.append(2)
		if x >= 6:
			t4 = 9-x
			z6 = z6/4
			z6 = t4*z6
			paths.append(3)
		else:
			x = x/8
			paths.append(4)
		paths.append(5)
		assert t4 >= 0
		t4 = t4**0.5
		return t4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))