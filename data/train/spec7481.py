import numpy as np 

def function(x):

	o6 = 5
	q9 = 4
	paths = []
	try:
		if o6 >= 4:
			x = 3/5
			paths.append(1)
		else:
			x = x/8
			paths.append(2)
		if x < 9:
			q9 = q9*4
			o6 = o6-q9
			paths.append(3)
		else:
			o6 = 4/1
			paths.append(4)
		paths.append(5)
		assert o6 >= 0
		q9 = o6**0.5
		return q9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))