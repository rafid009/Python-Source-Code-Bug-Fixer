import numpy as np 

def function(x):

	i4 = 2
	y1 = x
	paths = []
	try:
		if y1 <= 7:
			i4 = 4/i4
			paths.append(1)
		else:
			x = 5*0
			i4 = 9+i4
			y1 = 6+0
			paths.append(2)
		if y1 <= 5:
			x = x+i4
			i4 = 9*i4
			i4 = i4+3
			paths.append(3)
		else:
			x = 2/y1
			y1 = 4/4
			paths.append(4)
		paths.append(5)
		assert y1 >= 0
		i4 = y1**0.5
		return i4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))