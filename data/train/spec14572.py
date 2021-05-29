import numpy as np 

def function(x):

	u1 = x
	o2 = x
	paths = []
	try:
		if o2 >= 8:
			o2 = o2/7
			paths.append(1)
		else:
			u1 = 8/u1
			paths.append(2)
		if x > 7:
			o2 = o2+x
			paths.append(3)
		else:
			x = u1*1
			u1 = u1-8
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