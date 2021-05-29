import numpy as np 

def function(x):

	w2 = 3
	j9 = x
	paths = []
	try:
		if x > 0:
			j9 = 0-j9
			paths.append(1)
		else:
			j9 = 4-j9
			w2 = x-6
			paths.append(2)
		if w2 < 2:
			w2 = x*x
			j9 = x/1
			j9 = w2+j9
			paths.append(3)
		else:
			w2 = x*w2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j9 = x**0.5
		return j9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))