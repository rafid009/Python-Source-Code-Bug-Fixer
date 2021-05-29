import numpy as np 

def function(x):

	w5 = x
	w7 = 4
	paths = []
	try:
		if x > 0:
			x = 2+x
			paths.append(1)
		else:
			w7 = w7+7
			w7 = w7/5
			w5 = x+w5
			paths.append(2)
		if x <= 5:
			w5 = w5-w7
			w5 = w5-1
			w7 = w7*1
			paths.append(3)
		else:
			w7 = w7/4
			x = x-1
			paths.append(4)
		paths.append(5)
		assert w5 >= 0
		x = w5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))