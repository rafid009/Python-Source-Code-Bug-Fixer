import numpy as np 

def function(x):

	i0 = x
	y7 = 6
	paths = []
	try:
		if i0 < 0:
			i0 = i0/i0
			i0 = 0-i0
			paths.append(1)
		else:
			x = x/3
			y7 = x*i0
			x = x+1
			paths.append(2)
		if y7 <= 4:
			x = x*6
			paths.append(3)
		else:
			x = 2/7
			paths.append(4)
		paths.append(5)
		assert i0 >= 0
		x = i0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))