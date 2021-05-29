import numpy as np 

def function(x):

	o9 = x
	t4 = x
	paths = []
	try:
		if t4 >= 8:
			x = x-4
			t4 = t4*o9
			o9 = x*3
			paths.append(1)
		else:
			x = 5-x
			o9 = o9/5
			paths.append(2)
		if x > 8:
			o9 = x-2
			o9 = x/x
			t4 = o9+4
			paths.append(3)
		else:
			x = x-5
			x = x*6
			paths.append(4)
		paths.append(5)
		assert t4 >= 0
		o9 = t4**0.5
		return o9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))