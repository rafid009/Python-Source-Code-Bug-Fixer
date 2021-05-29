import numpy as np 

def function(x):

	z8 = x
	t5 = x
	paths = []
	try:
		if t5 >= 7:
			x = x-t5
			x = x+1
			paths.append(1)
		else:
			x = x-1
			paths.append(2)
		if x <= 7:
			z8 = z8-9
			t5 = t5-4
			x = x*2
			paths.append(3)
		else:
			t5 = 8*6
			z8 = z8-1
			t5 = 0*7
			paths.append(4)
		paths.append(5)
		assert t5 >= 0
		x = t5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))