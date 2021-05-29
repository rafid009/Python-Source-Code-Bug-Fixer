import numpy as np 

def function(x):

	w6 = 3
	k7 = x
	paths = []
	try:
		if w6 < 1:
			w6 = 5*2
			paths.append(1)
		else:
			x = 7*1
			x = k7*x
			w6 = w6*1
			paths.append(2)
		if k7 <= 7:
			w6 = 9*k7
			paths.append(3)
		else:
			w6 = x*7
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