import numpy as np 

def function(x):

	w2 = 6
	v2 = 5
	paths = []
	try:
		if v2 < 5:
			v2 = 1+1
			x = x+7
			paths.append(1)
		else:
			v2 = 4-9
			paths.append(2)
		if x <= 1:
			v2 = 6+8
			paths.append(3)
		else:
			w2 = x/9
			v2 = v2/6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))