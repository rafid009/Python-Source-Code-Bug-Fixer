import numpy as np 

def function(x):

	w2 = x
	i7 = 4
	paths = []
	try:
		if i7 <= 3:
			x = x*6
			w2 = 2+5
			x = i7-x
			paths.append(1)
		else:
			w2 = w2*7
			i7 = i7*x
			paths.append(2)
		if w2 <= 7:
			i7 = 2/x
			w2 = w2/2
			x = 9/w2
			paths.append(3)
		else:
			x = x/6
			paths.append(4)
		paths.append(5)
		assert i7 >= 0
		x = i7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))