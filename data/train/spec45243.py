import numpy as np 

def function(x):

	t3 = x
	w6 = x
	x = 2
	paths = []
	try:
		if x >= 8:
			x = x-5
			x = 6/w6
			w6 = t3/w6
			paths.append(1)
		else:
			w6 = 5-1
			w6 = 5+8
			paths.append(2)
		if t3 <= 7:
			x = x/7
			paths.append(3)
		else:
			x = 7-2
			paths.append(4)
		paths.append(5)
		assert t3 >= 0
		x = t3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))