import numpy as np 

def function(x):

	j6 = 6
	o2 = 7
	paths = []
	try:
		if x >= 3:
			x = o2*4
			x = x/x
			paths.append(1)
		else:
			o2 = j6-5
			o2 = j6*3
			paths.append(2)
		if o2 < 2:
			x = 7-3
			o2 = j6+2
			paths.append(3)
		else:
			x = x*o2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j6 = x**0.5
		return j6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))