import numpy as np 

def function(x):

	b0 = 1
	w1 = x
	paths = []
	try:
		if b0 > 2:
			b0 = 3+b0
			paths.append(1)
		else:
			b0 = 7*4
			paths.append(2)
		if x >= 0:
			x = x/3
			b0 = x/6
			w1 = w1*1
			paths.append(3)
		else:
			b0 = b0-8
			x = x+x
			b0 = w1+7
			paths.append(4)
		paths.append(5)
		assert b0 >= 0
		x = b0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))