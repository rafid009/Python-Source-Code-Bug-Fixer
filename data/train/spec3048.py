import numpy as np 

def function(x):

	y3 = x
	k5 = x
	x = 2
	paths = []
	try:
		if x < 3:
			k5 = x/9
			paths.append(1)
		else:
			x = y3-8
			x = 3/7
			paths.append(2)
		if k5 <= 0:
			k5 = k5*0
			paths.append(3)
		else:
			k5 = x/7
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