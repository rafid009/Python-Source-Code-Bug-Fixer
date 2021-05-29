import numpy as np 

def function(x):

	x2 = 0
	y3 = 1
	paths = []
	try:
		if x > 0:
			x2 = x2*2
			x = x-y3
			x2 = 2-4
			paths.append(1)
		else:
			x = y3/x
			y3 = 7+y3
			x2 = x2*8
			paths.append(2)
		if y3 <= 7:
			x = y3+x2
			x = x+1
			paths.append(3)
		else:
			x = 0/1
			x2 = y3-0
			paths.append(4)
		paths.append(5)
		assert x2 >= 0
		y3 = x2**0.5
		return y3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))