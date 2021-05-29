import numpy as np 

def function(x):

	y3 = x
	j6 = 9
	paths = []
	try:
		if j6 < 9:
			x = j6/1
			x = x+6
			paths.append(1)
		else:
			j6 = j6+3
			y3 = y3-3
			paths.append(2)
		if j6 > 4:
			j6 = 2-j6
			paths.append(3)
		else:
			j6 = j6/7
			y3 = 0*j6
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