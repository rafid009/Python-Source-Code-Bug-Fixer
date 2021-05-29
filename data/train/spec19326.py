import numpy as np 

def function(x):

	j1 = 8
	o6 = x
	paths = []
	try:
		if j1 <= 6:
			o6 = j1-8
			o6 = o6-4
			paths.append(1)
		else:
			x = x/1
			j1 = o6*j1
			paths.append(2)
		if o6 > 0:
			x = o6/9
			paths.append(3)
		else:
			x = x/3
			paths.append(4)
		paths.append(5)
		assert o6 >= 0
		x = o6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))