import numpy as np 

def function(x):

	y3 = 3
	n5 = x
	x = 8
	paths = []
	try:
		if x >= 8:
			y3 = n5/x
			paths.append(1)
		else:
			n5 = x/7
			y3 = 7*2
			paths.append(2)
		if y3 > 5:
			y3 = 7-n5
			x = 9-9
			x = x+0
			paths.append(3)
		else:
			n5 = n5-8
			x = x+1
			n5 = 1*n5
			paths.append(4)
		paths.append(5)
		assert y3 >= 0
		y3 = y3**0.5
		return y3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))