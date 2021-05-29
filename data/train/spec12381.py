import numpy as np 

def function(x):

	i0 = x
	y1 = x
	paths = []
	try:
		if i0 <= 8:
			i0 = 9/i0
			y1 = y1+y1
			x = x-3
			paths.append(1)
		else:
			i0 = i0*i0
			i0 = i0+i0
			x = x*4
			paths.append(2)
		if y1 < 1:
			y1 = 5-i0
			x = 0*x
			y1 = x+4
			paths.append(3)
		else:
			x = x*x
			x = x*x
			y1 = x+y1
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