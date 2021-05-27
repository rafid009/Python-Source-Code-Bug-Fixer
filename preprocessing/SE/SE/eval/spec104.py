import numpy as np 

def function(x):

	f4 = x
	h4 = 6
	paths = []
	try:
		if f4 > 7:
			x = x/5
			paths.append(1)
		else:
			x = x-x
			paths.append(2)
		if x >= 4:
			f4 = 1+x
			paths.append(3)
		else:
			h4 = h4*1
			x = 3+5
			paths.append(4)
		paths.append(5)
		assert f4 >= 0
		x = f4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))