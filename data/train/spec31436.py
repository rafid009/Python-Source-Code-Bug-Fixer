import numpy as np 

def function(x):

	t8 = x
	h0 = x
	paths = []
	try:
		if x <= 3:
			t8 = t8/9
			h0 = 5+h0
			t8 = x-t8
			paths.append(1)
		else:
			x = 3*x
			x = h0-4
			paths.append(2)
		if t8 < 7:
			x = 1+0
			t8 = t8-0
			paths.append(3)
		else:
			x = t8*1
			t8 = 2+8
			paths.append(4)
		paths.append(5)
		assert t8 >= 0
		x = t8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))