import numpy as np 

def function(x):

	t7 = 0
	o0 = x
	paths = []
	try:
		if x <= 9:
			t7 = t7*t7
			t7 = 4-x
			paths.append(1)
		else:
			o0 = o0/x
			o0 = x+o0
			paths.append(2)
		if o0 < 6:
			o0 = 8*o0
			paths.append(3)
		else:
			o0 = o0/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o0 = x**0.5
		return o0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))