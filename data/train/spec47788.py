import numpy as np 

def function(x):

	o1 = x
	t8 = 9
	paths = []
	try:
		if o1 >= 8:
			x = t8/t8
			t8 = t8+o1
			paths.append(1)
		else:
			t8 = t8+2
			o1 = o1+t8
			paths.append(2)
		if x > 7:
			x = 2/x
			paths.append(3)
		else:
			o1 = o1/8
			t8 = 3/x
			paths.append(4)
		paths.append(5)
		assert o1 >= 0
		x = o1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))