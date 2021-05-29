import numpy as np 

def function(x):

	q7 = 6
	o6 = x
	paths = []
	try:
		if x <= 0:
			o6 = q7-o6
			x = x+q7
			paths.append(1)
		else:
			q7 = o6-3
			o6 = o6/1
			q7 = 4-q7
			paths.append(2)
		if q7 < 7:
			x = x*8
			paths.append(3)
		else:
			x = 6/o6
			paths.append(4)
		paths.append(5)
		assert q7 >= 0
		x = q7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))