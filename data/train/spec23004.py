import numpy as np 

def function(x):

	g8 = x
	b8 = 3
	paths = []
	try:
		if b8 <= 8:
			g8 = g8*b8
			paths.append(1)
		else:
			g8 = 6/g8
			x = x-x
			x = 7/x
			paths.append(2)
		if x > 9:
			b8 = x*0
			b8 = b8-9
			paths.append(3)
		else:
			x = g8*7
			b8 = b8-b8
			paths.append(4)
		paths.append(5)
		assert g8 >= 0
		x = g8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))