import numpy as np 

def function(x):

	j4 = x
	y3 = 5
	paths = []
	try:
		if x <= 7:
			y3 = y3*y3
			y3 = y3-5
			j4 = j4*y3
			paths.append(1)
		else:
			j4 = x-3
			x = x+7
			paths.append(2)
		if j4 <= 5:
			y3 = j4-y3
			x = x+1
			x = j4+x
			paths.append(3)
		else:
			j4 = j4-1
			y3 = y3-j4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j4 = x**0.5
		return j4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))