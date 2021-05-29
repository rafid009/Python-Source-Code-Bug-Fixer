import numpy as np 

def function(x):

	y8 = x
	i3 = 2
	paths = []
	try:
		if i3 > 4:
			i3 = 0-1
			i3 = 2*8
			x = x+1
			paths.append(1)
		else:
			x = 9/7
			paths.append(2)
		if x >= 6:
			x = x+4
			y8 = 3/y8
			i3 = i3+x
			paths.append(3)
		else:
			x = 9*6
			i3 = y8+i3
			paths.append(4)
		paths.append(5)
		assert y8 >= 0
		i3 = y8**0.5
		return i3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))