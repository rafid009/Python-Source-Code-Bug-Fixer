import numpy as np 

def function(x):

	h8 = x
	t4 = x
	paths = []
	try:
		if t4 < 5:
			x = x*x
			paths.append(1)
		else:
			t4 = t4+t4
			paths.append(2)
		if h8 <= 3:
			h8 = 3-0
			h8 = 9/h8
			paths.append(3)
		else:
			h8 = h8*1
			paths.append(4)
		paths.append(5)
		assert t4 >= 0
		x = t4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))