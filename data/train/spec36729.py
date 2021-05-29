import numpy as np 

def function(x):

	o2 = x
	j5 = 4
	paths = []
	try:
		if x > 1:
			o2 = 6+1
			j5 = j5-6
			paths.append(1)
		else:
			j5 = j5+0
			paths.append(2)
		if x > 7:
			o2 = o2/x
			paths.append(3)
		else:
			j5 = 2+j5
			j5 = x*3
			x = x+j5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o2 = x**0.5
		return o2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))