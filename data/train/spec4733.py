import numpy as np 

def function(x):

	j1 = x
	y2 = x
	paths = []
	try:
		if x > 4:
			x = 4-x
			y2 = y2-x
			x = 5+x
			paths.append(1)
		else:
			x = 1/8
			j1 = j1/7
			y2 = j1-4
			paths.append(2)
		if y2 >= 5:
			j1 = 7/y2
			y2 = j1+x
			paths.append(3)
		else:
			x = 6*x
			y2 = y2+y2
			paths.append(4)
		paths.append(5)
		assert j1 >= 0
		y2 = j1**0.5
		return y2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))