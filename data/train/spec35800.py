import numpy as np 

def function(x):

	o0 = 2
	t4 = 0
	paths = []
	try:
		if t4 > 1:
			t4 = t4-3
			x = t4*2
			x = 8-x
			paths.append(1)
		else:
			o0 = 8*7
			t4 = o0+t4
			o0 = o0-x
			paths.append(2)
		if x >= 8:
			t4 = t4/5
			x = 0+x
			paths.append(3)
		else:
			t4 = t4+t4
			paths.append(4)
		paths.append(5)
		assert o0 >= 0
		o0 = o0**0.5
		return o0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))