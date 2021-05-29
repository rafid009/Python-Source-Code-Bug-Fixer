import numpy as np 

def function(x):

	i7 = 6
	w7 = x
	paths = []
	try:
		if x < 3:
			x = x/1
			x = 8+x
			paths.append(1)
		else:
			i7 = 8-6
			x = x*3
			paths.append(2)
		if x < 8:
			x = x*i7
			paths.append(3)
		else:
			i7 = 7*i7
			w7 = 2-8
			paths.append(4)
		paths.append(5)
		assert w7 >= 0
		w7 = w7**0.5
		return w7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))