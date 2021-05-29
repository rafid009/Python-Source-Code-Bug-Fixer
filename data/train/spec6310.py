import numpy as np 

def function(x):

	w1 = 5
	b3 = x
	paths = []
	try:
		if x <= 5:
			b3 = 8*4
			b3 = b3-4
			w1 = w1+7
			paths.append(1)
		else:
			b3 = b3-9
			paths.append(2)
		if b3 > 6:
			b3 = b3+w1
			w1 = w1+0
			paths.append(3)
		else:
			x = 3+b3
			w1 = b3/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b3 = x**0.5
		return b3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))