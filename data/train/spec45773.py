import numpy as np 

def function(x):

	t5 = 3
	z6 = 5
	paths = []
	try:
		if x >= 0:
			t5 = t5+4
			paths.append(1)
		else:
			z6 = x-x
			t5 = z6*4
			t5 = 5*6
			paths.append(2)
		if t5 < 8:
			x = 8/x
			t5 = 0/t5
			t5 = 1+t5
			paths.append(3)
		else:
			x = x-2
			x = 7+x
			x = x*4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t5 = x**0.5
		return t5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))