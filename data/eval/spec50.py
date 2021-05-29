import numpy as np 

def function(x):

	v8 = 0
	h2 = x
	paths = []
	try:
		if v8 >= 1:
			h2 = 3*8
			h2 = h2-5
			v8 = v8/9
			paths.append(1)
		else:
			v8 = 4*x
			v8 = x*6
			v8 = v8*1
			paths.append(2)
		if h2 <= 7:
			h2 = x*h2
			v8 = 2-v8
			paths.append(3)
		else:
			x = x/h2
			h2 = 3/h2
			h2 = h2+1
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