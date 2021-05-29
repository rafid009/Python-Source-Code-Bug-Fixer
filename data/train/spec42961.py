import numpy as np 

def function(x):

	t4 = x
	o0 = 1
	paths = []
	try:
		if x > 4:
			o0 = 2*o0
			t4 = t4*3
			paths.append(1)
		else:
			t4 = x*4
			t4 = t4-2
			paths.append(2)
		if t4 >= 2:
			o0 = 8+o0
			t4 = 2-t4
			t4 = 0+t4
			paths.append(3)
		else:
			t4 = t4/8
			x = 1+8
			paths.append(4)
		paths.append(5)
		assert t4 >= 0
		o0 = t4**0.5
		return o0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))