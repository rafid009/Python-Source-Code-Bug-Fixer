import numpy as np 

def function(x):

	w1 = x
	i7 = 6
	paths = []
	try:
		if w1 <= 3:
			w1 = 0/w1
			i7 = w1*i7
			i7 = 0+5
			paths.append(1)
		else:
			i7 = i7/w1
			paths.append(2)
		if x > 7:
			x = i7-x
			paths.append(3)
		else:
			x = x+2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w1 = x**0.5
		return w1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))