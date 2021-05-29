import numpy as np 

def function(x):

	n2 = x
	t8 = 5
	paths = []
	try:
		if n2 > 0:
			t8 = t8+x
			paths.append(1)
		else:
			t8 = x-0
			x = x-8
			n2 = x/6
			paths.append(2)
		if n2 >= 8:
			n2 = n2-n2
			t8 = x*t8
			paths.append(3)
		else:
			t8 = 1+x
			x = n2-t8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n2 = x**0.5
		return n2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))