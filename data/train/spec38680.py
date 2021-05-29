import numpy as np 

def function(x):

	v8 = x
	q5 = 5
	x = 7
	paths = []
	try:
		if q5 < 2:
			v8 = 3/v8
			v8 = 0/v8
			x = v8+6
			paths.append(1)
		else:
			x = 5-x
			paths.append(2)
		if v8 < 0:
			q5 = q5*5
			paths.append(3)
		else:
			v8 = 7-6
			q5 = q5+6
			paths.append(4)
		paths.append(5)
		assert v8 >= 0
		v8 = v8**0.5
		return v8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))