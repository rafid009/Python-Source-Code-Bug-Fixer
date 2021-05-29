import numpy as np 

def function(x):

	h4 = x
	f0 = 4
	paths = []
	try:
		if x > 4:
			h4 = h4+0
			f0 = 4-f0
			h4 = h4-x
			paths.append(1)
		else:
			f0 = 8-3
			paths.append(2)
		if x < 8:
			x = f0+x
			x = 1*x
			paths.append(3)
		else:
			x = x+8
			paths.append(4)
		paths.append(5)
		assert h4 >= 0
		f0 = h4**0.5
		return f0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))