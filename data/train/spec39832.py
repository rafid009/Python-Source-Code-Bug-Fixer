import numpy as np 

def function(x):

	o2 = x
	t8 = x
	paths = []
	try:
		if x >= 6:
			o2 = 8-x
			x = 6-x
			paths.append(1)
		else:
			x = x-9
			o2 = 5-o2
			paths.append(2)
		if o2 >= 9:
			o2 = o2*x
			x = 4*x
			paths.append(3)
		else:
			x = 8/5
			t8 = 4/x
			paths.append(4)
		paths.append(5)
		assert o2 >= 0
		t8 = o2**0.5
		return t8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))