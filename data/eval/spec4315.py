import numpy as np 

def function(x):

	i7 = 3
	w7 = x
	paths = []
	try:
		if i7 <= 0:
			i7 = i7*x
			i7 = i7*2
			w7 = 3*4
			paths.append(1)
		else:
			i7 = x*9
			i7 = i7/3
			paths.append(2)
		if w7 >= 9:
			x = 2*0
			w7 = w7+w7
			x = 3+3
			paths.append(3)
		else:
			x = x-8
			x = w7/x
			x = x*5
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