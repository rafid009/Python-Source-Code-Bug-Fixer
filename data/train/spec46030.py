import numpy as np 

def function(x):

	y1 = x
	b4 = x
	paths = []
	try:
		if y1 <= 5:
			x = 8-5
			x = x*8
			paths.append(1)
		else:
			b4 = b4-7
			y1 = y1/1
			paths.append(2)
		if b4 <= 4:
			y1 = 2-3
			y1 = y1*b4
			paths.append(3)
		else:
			y1 = 0-x
			y1 = b4-4
			x = x-2
			paths.append(4)
		paths.append(5)
		assert y1 >= 0
		b4 = y1**0.5
		return b4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))