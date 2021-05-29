import numpy as np 

def function(x):

	t0 = 4
	o7 = x
	paths = []
	try:
		if x > 7:
			o7 = o7+x
			paths.append(1)
		else:
			o7 = o7-4
			t0 = x-t0
			t0 = t0*9
			paths.append(2)
		if o7 < 3:
			x = 8-x
			paths.append(3)
		else:
			t0 = 4+1
			paths.append(4)
		paths.append(5)
		assert t0 >= 0
		x = t0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))