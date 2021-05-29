import numpy as np 

def function(x):

	i5 = 3
	x1 = x
	paths = []
	try:
		if x <= 6:
			x = 7-x
			x1 = x1-i5
			paths.append(1)
		else:
			i5 = x1*2
			i5 = i5+0
			x = x*0
			paths.append(2)
		if x >= 1:
			i5 = 2/i5
			x1 = x1/1
			x1 = 7/x1
			paths.append(3)
		else:
			x = 4-x
			x1 = 7-i5
			i5 = 9+i5
			paths.append(4)
		paths.append(5)
		assert x1 >= 0
		i5 = x1**0.5
		return i5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))