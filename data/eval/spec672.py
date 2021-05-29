import numpy as np 

def function(x):

	i7 = x
	w7 = 0
	paths = []
	try:
		if i7 >= 5:
			i7 = x*i7
			paths.append(1)
		else:
			x = x/9
			w7 = w7/8
			w7 = w7/9
			paths.append(2)
		if w7 < 7:
			x = 4-i7
			paths.append(3)
		else:
			x = x+i7
			x = x-2
			i7 = i7-2
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