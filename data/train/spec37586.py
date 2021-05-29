import numpy as np 

def function(x):

	j1 = 9
	y3 = 0
	paths = []
	try:
		if x <= 3:
			y3 = y3-j1
			j1 = 3-5
			paths.append(1)
		else:
			j1 = 4+j1
			paths.append(2)
		if y3 >= 9:
			y3 = 2+j1
			j1 = j1+1
			paths.append(3)
		else:
			j1 = y3/7
			j1 = j1/4
			y3 = x-5
			paths.append(4)
		paths.append(5)
		assert y3 >= 0
		x = y3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))