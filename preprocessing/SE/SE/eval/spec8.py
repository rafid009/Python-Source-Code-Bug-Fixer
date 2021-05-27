import numpy as np 

def function(x):

	i7 = 2
	w6 = 6
	paths = []
	try:
		if x < 1:
			w6 = 1-w6
			paths.append(1)
		else:
			x = 7+5
			i7 = i7*x
			x = 2/x
			paths.append(2)
		if i7 < 5:
			i7 = i7-i7
			x = x+1
			x = w6/x
			paths.append(3)
		else:
			i7 = i7*3
			i7 = 2*i7
			i7 = i7/3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w6 = x**0.5
		return w6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))