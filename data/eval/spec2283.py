import numpy as np 

def function(x):

	w5 = 2
	a7 = x
	paths = []
	try:
		if a7 < 5:
			x = x-5
			x = 0+1
			paths.append(1)
		else:
			w5 = w5-5
			paths.append(2)
		if a7 < 8:
			x = 2/3
			w5 = w5+9
			paths.append(3)
		else:
			w5 = 2-8
			paths.append(4)
		paths.append(5)
		assert a7 >= 0
		a7 = a7**0.5
		return a7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))