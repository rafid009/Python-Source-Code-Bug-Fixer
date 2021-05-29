import numpy as np 

def function(x):

	w1 = x
	a0 = 1
	paths = []
	try:
		if a0 > 4:
			w1 = 8*5
			paths.append(1)
		else:
			w1 = w1*2
			paths.append(2)
		if a0 <= 2:
			x = x+5
			paths.append(3)
		else:
			x = 1+x
			x = x+7
			w1 = w1-x
			paths.append(4)
		paths.append(5)
		assert w1 >= 0
		x = w1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))