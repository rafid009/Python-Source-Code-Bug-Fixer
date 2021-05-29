import numpy as np 

def function(x):

	i3 = 7
	y2 = x
	paths = []
	try:
		if x < 3:
			y2 = y2*8
			y2 = 8-y2
			x = x+2
			paths.append(1)
		else:
			y2 = y2/9
			paths.append(2)
		if y2 <= 0:
			x = i3*x
			paths.append(3)
		else:
			i3 = i3/3
			y2 = 9*y2
			y2 = y2+0
			paths.append(4)
		paths.append(5)
		assert y2 >= 0
		x = y2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))