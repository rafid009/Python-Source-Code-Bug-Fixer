import numpy as np 

def function(x):

	o1 = 8
	t0 = 4
	paths = []
	try:
		if x < 1:
			t0 = t0*9
			x = o1/3
			paths.append(1)
		else:
			t0 = 7/t0
			o1 = 0-o1
			o1 = x/o1
			paths.append(2)
		if x >= 2:
			o1 = o1+8
			o1 = 8/o1
			paths.append(3)
		else:
			o1 = o1-0
			o1 = o1*8
			paths.append(4)
		paths.append(5)
		assert o1 >= 0
		t0 = o1**0.5
		return t0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))