import numpy as np 

def function(x):

	w1 = 6
	b0 = x
	paths = []
	try:
		if x < 9:
			x = w1+x
			x = 1*x
			paths.append(1)
		else:
			b0 = b0/1
			b0 = w1+b0
			paths.append(2)
		if w1 <= 5:
			x = 8/x
			w1 = 0*3
			paths.append(3)
		else:
			w1 = w1/9
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