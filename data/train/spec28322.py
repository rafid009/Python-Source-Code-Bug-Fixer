import numpy as np 

def function(x):

	o1 = x
	q7 = x
	paths = []
	try:
		if x <= 2:
			x = 0+1
			o1 = o1-5
			paths.append(1)
		else:
			o1 = o1*3
			x = x+q7
			o1 = 3-o1
			paths.append(2)
		if o1 >= 2:
			o1 = x+q7
			paths.append(3)
		else:
			x = o1*6
			paths.append(4)
		paths.append(5)
		assert o1 >= 0
		q7 = o1**0.5
		return q7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))