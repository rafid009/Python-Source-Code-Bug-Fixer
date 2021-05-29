import numpy as np 

def function(x):

	y6 = 9
	i1 = x
	paths = []
	try:
		if x < 9:
			y6 = y6/x
			y6 = x*y6
			i1 = 8*y6
			paths.append(1)
		else:
			i1 = 0-1
			x = 4/x
			x = x+5
			paths.append(2)
		if y6 > 0:
			x = x-7
			x = 6/i1
			paths.append(3)
		else:
			y6 = 6*y6
			i1 = i1*0
			paths.append(4)
		paths.append(5)
		assert i1 >= 0
		i1 = i1**0.5
		return i1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))