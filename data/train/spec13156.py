import numpy as np 

def function(x):

	x6 = x
	g8 = x
	paths = []
	try:
		if g8 >= 9:
			x = 7+2
			x6 = x6+8
			x = 8*x
			paths.append(1)
		else:
			x6 = 2*g8
			paths.append(2)
		if g8 < 3:
			x = x/3
			x6 = x*x6
			paths.append(3)
		else:
			x = 1*x
			x = 4/g8
			x6 = g8+1
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