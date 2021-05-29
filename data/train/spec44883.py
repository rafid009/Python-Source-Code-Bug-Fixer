import numpy as np 

def function(x):

	i9 = 7
	y1 = 2
	paths = []
	try:
		if y1 > 2:
			i9 = y1/9
			paths.append(1)
		else:
			y1 = i9+i9
			i9 = i9/x
			i9 = i9/9
			paths.append(2)
		if i9 <= 7:
			y1 = y1+1
			x = 4+2
			paths.append(3)
		else:
			x = x+i9
			x = i9*x
			paths.append(4)
		paths.append(5)
		assert i9 >= 0
		x = i9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))