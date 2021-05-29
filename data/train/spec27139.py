import numpy as np 

def function(x):

	i7 = x
	w7 = 8
	paths = []
	try:
		if i7 <= 5:
			w7 = w7+i7
			w7 = w7*4
			i7 = 7/4
			paths.append(1)
		else:
			x = 7*4
			x = x+1
			x = x/5
			paths.append(2)
		if w7 <= 0:
			i7 = i7*8
			i7 = 1-4
			paths.append(3)
		else:
			x = x+9
			x = w7/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i7 = x**0.5
		return i7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))