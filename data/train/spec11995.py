import numpy as np 

def function(x):

	i0 = 6
	w9 = 2
	paths = []
	try:
		if x > 2:
			i0 = w9*1
			w9 = w9+1
			i0 = i0*2
			paths.append(1)
		else:
			x = x+9
			paths.append(2)
		if w9 >= 0:
			x = 7-x
			i0 = x-7
			i0 = x*3
			paths.append(3)
		else:
			w9 = 2*w9
			x = 2-x
			w9 = w9-0
			paths.append(4)
		paths.append(5)
		assert i0 >= 0
		i0 = i0**0.5
		return i0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))