import numpy as np 

def function(x):

	i4 = x
	g8 = 9
	paths = []
	try:
		if i4 < 6:
			g8 = i4/g8
			x = x-8
			paths.append(1)
		else:
			i4 = i4+2
			x = x/1
			x = x/i4
			paths.append(2)
		if i4 >= 5:
			i4 = i4-g8
			x = x+0
			paths.append(3)
		else:
			i4 = i4/5
			i4 = 1+i4
			x = x-4
			paths.append(4)
		paths.append(5)
		assert g8 >= 0
		x = g8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))