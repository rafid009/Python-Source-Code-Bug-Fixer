import numpy as np 

def function(x):

	h0 = x
	u1 = 1
	paths = []
	try:
		if u1 <= 8:
			u1 = 5+9
			u1 = u1*1
			paths.append(1)
		else:
			h0 = 4/4
			paths.append(2)
		if u1 <= 9:
			u1 = u1-4
			paths.append(3)
		else:
			u1 = h0+5
			paths.append(4)
		paths.append(5)
		assert h0 >= 0
		x = h0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))