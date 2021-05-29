import numpy as np 

def function(x):

	t4 = 9
	h2 = x
	paths = []
	try:
		if x < 4:
			t4 = t4*2
			x = x+9
			paths.append(1)
		else:
			t4 = t4+1
			h2 = 2-h2
			paths.append(2)
		if x < 1:
			t4 = h2*t4
			paths.append(3)
		else:
			t4 = h2/t4
			t4 = 7/1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))