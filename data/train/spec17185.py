import numpy as np 

def function(x):

	q4 = 3
	o2 = x
	paths = []
	try:
		if o2 < 1:
			x = 3-x
			paths.append(1)
		else:
			o2 = q4/7
			o2 = q4*3
			q4 = q4-x
			paths.append(2)
		if o2 <= 0:
			o2 = x*9
			o2 = 1/o2
			paths.append(3)
		else:
			o2 = 2-o2
			q4 = 8/q4
			paths.append(4)
		paths.append(5)
		assert q4 >= 0
		o2 = q4**0.5
		return o2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))