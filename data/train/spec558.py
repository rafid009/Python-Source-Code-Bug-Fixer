import numpy as np 

def function(x):

	o6 = 1
	t0 = x
	paths = []
	try:
		if t0 < 6:
			t0 = 5/t0
			t0 = t0+x
			t0 = t0/8
			paths.append(1)
		else:
			o6 = t0/9
			x = 8/x
			x = 1/2
			paths.append(2)
		if o6 >= 5:
			o6 = 5-o6
			x = 8/x
			paths.append(3)
		else:
			o6 = 2/o6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t0 = x**0.5
		return t0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))