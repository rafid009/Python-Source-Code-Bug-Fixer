import numpy as np 

def function(x):

	a1 = x
	y7 = 7
	paths = []
	try:
		if x >= 3:
			a1 = a1-2
			x = x/9
			paths.append(1)
		else:
			a1 = a1/8
			y7 = a1/a1
			x = 1+x
			paths.append(2)
		if x >= 8:
			a1 = y7*a1
			x = y7/3
			y7 = y7*0
			paths.append(3)
		else:
			y7 = y7+7
			y7 = x+7
			y7 = y7*7
			paths.append(4)
		paths.append(5)
		assert a1 >= 0
		y7 = a1**0.5
		return y7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))