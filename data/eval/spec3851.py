import numpy as np 

def function(x):

	e6 = x
	o1 = x
	paths = []
	try:
		if x <= 3:
			x = x*1
			paths.append(1)
		else:
			e6 = 2-5
			x = x-7
			paths.append(2)
		if e6 >= 8:
			o1 = 6/x
			e6 = e6-8
			o1 = 0/o1
			paths.append(3)
		else:
			e6 = 1-o1
			x = x+7
			paths.append(4)
		paths.append(5)
		assert o1 >= 0
		x = o1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))