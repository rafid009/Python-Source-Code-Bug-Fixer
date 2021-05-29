import numpy as np 

def function(x):

	b1 = 8
	o9 = 7
	paths = []
	try:
		if o9 <= 5:
			x = 0*x
			paths.append(1)
		else:
			b1 = 3-o9
			x = 6-x
			paths.append(2)
		if x < 5:
			x = 4-x
			paths.append(3)
		else:
			o9 = x*3
			x = x*4
			paths.append(4)
		paths.append(5)
		assert b1 >= 0
		x = b1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))