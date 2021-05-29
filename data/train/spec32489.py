import numpy as np 

def function(x):

	f5 = 3
	h8 = 8
	paths = []
	try:
		if h8 > 6:
			f5 = 1*f5
			h8 = h8/1
			x = 2+x
			paths.append(1)
		else:
			x = x+7
			x = x*x
			paths.append(2)
		if f5 >= 5:
			f5 = x*1
			paths.append(3)
		else:
			x = h8-x
			x = x/3
			x = x/4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f5 = x**0.5
		return f5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))