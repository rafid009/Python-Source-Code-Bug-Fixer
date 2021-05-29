import numpy as np 

def function(x):

	o4 = 3
	t0 = x
	paths = []
	try:
		if x >= 7:
			o4 = 1-o4
			x = 5/t0
			paths.append(1)
		else:
			t0 = 0/t0
			x = x-0
			x = 4*x
			paths.append(2)
		if o4 >= 5:
			o4 = x+1
			x = x-7
			x = x+4
			paths.append(3)
		else:
			x = x/o4
			paths.append(4)
		paths.append(5)
		assert o4 >= 0
		t0 = o4**0.5
		return t0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))