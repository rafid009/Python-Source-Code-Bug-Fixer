import numpy as np 

def function(x):

	x5 = x
	d7 = x
	x = 8
	paths = []
	try:
		if d7 < 7:
			x = x-9
			x5 = x5*1
			paths.append(1)
		else:
			x = x*2
			x = x5*8
			paths.append(2)
		if x5 < 5:
			d7 = x5*x5
			paths.append(3)
		else:
			x = 9-8
			x = x-7
			d7 = 5+x5
			paths.append(4)
		paths.append(5)
		assert x5 >= 0
		x5 = x5**0.5
		return x5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))