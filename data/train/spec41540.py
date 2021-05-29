import numpy as np 

def function(x):

	f1 = x
	h4 = x
	paths = []
	try:
		if x < 6:
			x = 8-9
			paths.append(1)
		else:
			f1 = 8/f1
			paths.append(2)
		if f1 <= 6:
			x = x+5
			h4 = h4/6
			paths.append(3)
		else:
			f1 = f1-8
			x = x/8
			paths.append(4)
		paths.append(5)
		assert f1 >= 0
		x = f1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))