import numpy as np 

def function(x):

	o9 = x
	t3 = x
	paths = []
	try:
		if t3 > 7:
			o9 = 8*x
			paths.append(1)
		else:
			o9 = o9-8
			t3 = 1-5
			paths.append(2)
		if o9 >= 9:
			x = 9/x
			paths.append(3)
		else:
			x = 4/5
			paths.append(4)
		paths.append(5)
		assert o9 >= 0
		x = o9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))