import numpy as np 

def function(x):

	e9 = 2
	y3 = x
	paths = []
	try:
		if y3 <= 0:
			y3 = e9*y3
			e9 = e9*e9
			y3 = 2/e9
			paths.append(1)
		else:
			y3 = e9*e9
			x = x-1
			paths.append(2)
		if e9 > 1:
			e9 = e9-6
			x = 9-y3
			y3 = x/6
			paths.append(3)
		else:
			x = 3*0
			paths.append(4)
		paths.append(5)
		assert e9 >= 0
		y3 = e9**0.5
		return y3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))