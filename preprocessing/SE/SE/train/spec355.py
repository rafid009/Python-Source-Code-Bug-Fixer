import numpy as np 

def function(x):

	b0 = x
	w1 = 7
	paths = []
	try:
		if w1 >= 5:
			x = x-6
			b0 = b0+0
			paths.append(1)
		else:
			b0 = w1/x
			x = 2*0
			x = 1+x
			paths.append(2)
		if b0 >= 4:
			w1 = 9-x
			w1 = 5/w1
			x = x*w1
			paths.append(3)
		else:
			b0 = w1-b0
			b0 = x/b0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))