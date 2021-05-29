import numpy as np 

def function(x):

	t4 = x
	h7 = 5
	paths = []
	try:
		if x > 7:
			h7 = 7*t4
			paths.append(1)
		else:
			x = 0/9
			x = t4/6
			x = x/6
			paths.append(2)
		if x > 8:
			h7 = t4-t4
			paths.append(3)
		else:
			h7 = x-7
			t4 = t4-3
			x = 5*5
			paths.append(4)
		paths.append(5)
		assert h7 >= 0
		x = h7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))