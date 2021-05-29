import numpy as np 

def function(x):

	w6 = x
	x6 = x
	paths = []
	try:
		if w6 > 4:
			x = x+x6
			paths.append(1)
		else:
			x = x-7
			paths.append(2)
		if w6 < 2:
			x = x*w6
			x = 2-8
			paths.append(3)
		else:
			w6 = w6-2
			x = x*w6
			x = x*6
			paths.append(4)
		paths.append(5)
		assert w6 >= 0
		x = w6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))