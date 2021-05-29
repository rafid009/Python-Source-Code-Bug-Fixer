import numpy as np 

def function(x):

	y7 = 5
	f6 = 7
	paths = []
	try:
		if y7 > 5:
			f6 = 5+f6
			y7 = f6-f6
			paths.append(1)
		else:
			x = x/2
			paths.append(2)
		if y7 <= 9:
			f6 = x/y7
			paths.append(3)
		else:
			x = x+8
			x = x+x
			x = 3+7
			paths.append(4)
		paths.append(5)
		assert f6 >= 0
		y7 = f6**0.5
		return y7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))