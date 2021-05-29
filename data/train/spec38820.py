import numpy as np 

def function(x):

	i9 = x
	j5 = x
	paths = []
	try:
		if x > 0:
			i9 = i9*9
			x = x*3
			i9 = 8/x
			paths.append(1)
		else:
			i9 = 7+i9
			paths.append(2)
		if x <= 9:
			i9 = i9/x
			j5 = j5+9
			paths.append(3)
		else:
			x = j5*j5
			x = i9*8
			i9 = 8/i9
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