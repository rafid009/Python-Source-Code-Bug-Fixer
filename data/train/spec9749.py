import numpy as np 

def function(x):

	y8 = x
	w9 = x
	paths = []
	try:
		if x > 0:
			w9 = w9-w9
			w9 = 5*8
			y8 = y8+9
			paths.append(1)
		else:
			w9 = 5/6
			paths.append(2)
		if x >= 7:
			w9 = 2+0
			x = x*1
			w9 = w9-8
			paths.append(3)
		else:
			y8 = 6-0
			x = 4*4
			paths.append(4)
		paths.append(5)
		assert w9 >= 0
		y8 = w9**0.5
		return y8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))