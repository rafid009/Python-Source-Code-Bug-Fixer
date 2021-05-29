import numpy as np 

def function(x):

	w6 = 3
	i7 = x
	paths = []
	try:
		if x > 4:
			x = x*i7
			paths.append(1)
		else:
			i7 = i7/i7
			paths.append(2)
		if i7 < 6:
			i7 = i7-w6
			paths.append(3)
		else:
			x = x/x
			paths.append(4)
		paths.append(5)
		assert i7 >= 0
		w6 = i7**0.5
		return w6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))