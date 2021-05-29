import numpy as np 

def function(x):

	z7 = x
	t5 = x
	x = x
	paths = []
	try:
		if t5 <= 5:
			t5 = x+5
			paths.append(1)
		else:
			t5 = t5*6
			t5 = 0/4
			t5 = x*t5
			paths.append(2)
		if z7 >= 7:
			x = 5-x
			z7 = z7-6
			paths.append(3)
		else:
			x = 6/x
			z7 = 7/z7
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