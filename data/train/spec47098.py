import numpy as np 

def function(x):

	w6 = 7
	x6 = 7
	paths = []
	try:
		if x6 <= 6:
			w6 = x*5
			paths.append(1)
		else:
			w6 = x-x
			x = 7*w6
			w6 = x6*3
			paths.append(2)
		if x < 8:
			x6 = 3-x6
			x6 = 2+x6
			paths.append(3)
		else:
			w6 = 0+w6
			x6 = 2/w6
			w6 = 1+w6
			paths.append(4)
		paths.append(5)
		assert x6 >= 0
		w6 = x6**0.5
		return w6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))