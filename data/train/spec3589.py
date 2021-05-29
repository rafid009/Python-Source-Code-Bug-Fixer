import numpy as np 

def function(x):

	o5 = 1
	u7 = 8
	paths = []
	try:
		if x <= 0:
			x = x/o5
			paths.append(1)
		else:
			x = x*x
			paths.append(2)
		if o5 >= 2:
			u7 = u7+5
			paths.append(3)
		else:
			x = x+x
			o5 = o5-9
			u7 = 4*8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u7 = x**0.5
		return u7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))