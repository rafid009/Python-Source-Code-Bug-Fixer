import numpy as np 

def function(x):

	o2 = 6
	u9 = x
	paths = []
	try:
		if o2 < 4:
			x = 2/u9
			x = x-4
			x = x/1
			paths.append(1)
		else:
			x = x+9
			paths.append(2)
		if u9 >= 9:
			u9 = u9*x
			o2 = 2+o2
			o2 = u9-o2
			paths.append(3)
		else:
			u9 = x+u9
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