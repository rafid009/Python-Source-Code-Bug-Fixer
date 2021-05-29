import numpy as np 

def function(x):

	t0 = 2
	o2 = 7
	paths = []
	try:
		if x < 2:
			x = o2+x
			x = x-o2
			o2 = 8*o2
			paths.append(1)
		else:
			x = x-o2
			x = x+3
			o2 = t0-9
			paths.append(2)
		if o2 <= 9:
			t0 = x-t0
			t0 = 8*t0
			paths.append(3)
		else:
			x = x/o2
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