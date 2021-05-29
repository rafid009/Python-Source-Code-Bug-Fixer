import numpy as np 

def function(x):

	g8 = x
	r7 = 5
	paths = []
	try:
		if x <= 5:
			x = x+3
			x = x-6
			r7 = 7+6
			paths.append(1)
		else:
			x = x/r7
			x = x/r7
			g8 = g8+1
			paths.append(2)
		if x < 8:
			x = x+8
			r7 = r7/9
			paths.append(3)
		else:
			r7 = r7/g8
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