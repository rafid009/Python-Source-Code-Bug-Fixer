import numpy as np 

def function(x):

	q4 = x
	o6 = x
	paths = []
	try:
		if x >= 7:
			q4 = q4-9
			o6 = o6/o6
			paths.append(1)
		else:
			o6 = o6+5
			o6 = o6+q4
			q4 = q4+x
			paths.append(2)
		if q4 < 7:
			o6 = 1+q4
			paths.append(3)
		else:
			x = x-5
			o6 = 4/o6
			x = x*x
			paths.append(4)
		paths.append(5)
		assert o6 >= 0
		x = o6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))