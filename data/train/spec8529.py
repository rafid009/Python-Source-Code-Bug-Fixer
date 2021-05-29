import numpy as np 

def function(x):

	a7 = x
	w7 = 5
	paths = []
	try:
		if a7 > 9:
			x = x*2
			paths.append(1)
		else:
			x = w7+x
			paths.append(2)
		if x <= 0:
			a7 = a7+a7
			w7 = 2/w7
			paths.append(3)
		else:
			x = 4*x
			x = x+1
			w7 = 4+0
			paths.append(4)
		paths.append(5)
		assert a7 >= 0
		x = a7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))