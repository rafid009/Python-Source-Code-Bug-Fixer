import numpy as np 

def function(x):

	o2 = 8
	j9 = 9
	paths = []
	try:
		if x > 6:
			j9 = x-j9
			x = j9/x
			paths.append(1)
		else:
			x = x+x
			j9 = 0+x
			x = 2/x
			paths.append(2)
		if j9 > 2:
			o2 = 3*0
			paths.append(3)
		else:
			o2 = 2/o2
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