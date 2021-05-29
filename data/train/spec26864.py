import numpy as np 

def function(x):

	y1 = x
	a5 = x
	paths = []
	try:
		if x < 3:
			y1 = y1*a5
			y1 = y1*y1
			x = x-7
			paths.append(1)
		else:
			a5 = 3-8
			a5 = 2+x
			paths.append(2)
		if a5 <= 4:
			a5 = a5*2
			x = a5/6
			paths.append(3)
		else:
			x = a5+x
			y1 = y1*4
			paths.append(4)
		paths.append(5)
		assert a5 >= 0
		x = a5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))