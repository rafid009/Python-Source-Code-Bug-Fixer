import numpy as np 

def function(x):

	w1 = x
	b6 = 6
	x = 4
	paths = []
	try:
		if w1 < 3:
			b6 = w1+1
			paths.append(1)
		else:
			b6 = 9+0
			w1 = w1+3
			w1 = 0+w1
			paths.append(2)
		if w1 > 1:
			w1 = w1-3
			w1 = w1/3
			paths.append(3)
		else:
			b6 = b6+2
			b6 = b6/7
			paths.append(4)
		paths.append(5)
		assert w1 >= 0
		x = w1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))