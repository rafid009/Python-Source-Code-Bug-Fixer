import numpy as np 

def function(x):

	f4 = 2
	h0 = 4
	paths = []
	try:
		if f4 > 3:
			h0 = f4+6
			paths.append(1)
		else:
			h0 = 3/6
			f4 = f4*8
			paths.append(2)
		if f4 <= 4:
			x = x+f4
			x = 1+x
			paths.append(3)
		else:
			h0 = h0-f4
			f4 = 4-f4
			paths.append(4)
		paths.append(5)
		assert f4 >= 0
		f4 = f4**0.5
		return f4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))