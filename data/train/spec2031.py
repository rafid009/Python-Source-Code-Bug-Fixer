import numpy as np 

def function(x):

	o4 = x
	q7 = x
	paths = []
	try:
		if x <= 8:
			q7 = q7-x
			q7 = q7-5
			x = 9/o4
			paths.append(1)
		else:
			x = x*0
			o4 = 1-o4
			paths.append(2)
		if x < 8:
			o4 = o4*5
			paths.append(3)
		else:
			q7 = q7-x
			paths.append(4)
		paths.append(5)
		assert q7 >= 0
		o4 = q7**0.5
		return o4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))