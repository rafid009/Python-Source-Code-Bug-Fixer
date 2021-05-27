import numpy as np 

def function(x):

	j7 = 8
	o2 = x
	paths = []
	try:
		if o2 <= 0:
			x = 6-x
			j7 = 9/8
			paths.append(1)
		else:
			j7 = j7-j7
			x = 2-x
			x = x-3
			paths.append(2)
		if o2 < 7:
			o2 = 2*2
			j7 = 1+j7
			paths.append(3)
		else:
			o2 = 4-o2
			j7 = x-j7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j7 = x**0.5
		return j7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))