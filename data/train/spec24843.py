import numpy as np 

def function(x):

	y4 = x
	i0 = 6
	paths = []
	try:
		if x < 7:
			x = 0+x
			y4 = i0*1
			paths.append(1)
		else:
			x = x*8
			y4 = y4+4
			y4 = x*5
			paths.append(2)
		if i0 <= 4:
			x = x*x
			x = y4-x
			paths.append(3)
		else:
			i0 = i0/4
			x = x-5
			y4 = y4/4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y4 = x**0.5
		return y4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))