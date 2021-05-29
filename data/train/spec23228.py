import numpy as np 

def function(x):

	x6 = 9
	w9 = x
	x = x
	paths = []
	try:
		if x6 < 4:
			x6 = x6/2
			x = x*4
			paths.append(1)
		else:
			x = x-2
			w9 = w9/1
			paths.append(2)
		if w9 >= 7:
			x6 = 5*1
			x = x/2
			x = x6*x
			paths.append(3)
		else:
			x = x*x
			paths.append(4)
		paths.append(5)
		assert w9 >= 0
		x6 = w9**0.5
		return x6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))