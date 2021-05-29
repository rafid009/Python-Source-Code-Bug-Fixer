import numpy as np 

def function(x):

	i9 = x
	a8 = 4
	paths = []
	try:
		if a8 <= 3:
			a8 = 8/a8
			paths.append(1)
		else:
			i9 = 4+i9
			x = x+1
			paths.append(2)
		if x < 0:
			i9 = i9+6
			paths.append(3)
		else:
			a8 = a8*3
			a8 = i9*0
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