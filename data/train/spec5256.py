import numpy as np 

def function(x):

	o5 = 0
	q5 = x
	paths = []
	try:
		if x >= 8:
			o5 = 8-8
			paths.append(1)
		else:
			x = x+o5
			o5 = o5*9
			o5 = o5+x
			paths.append(2)
		if q5 > 8:
			x = 5-x
			paths.append(3)
		else:
			o5 = 1+o5
			o5 = 6+o5
			paths.append(4)
		paths.append(5)
		assert q5 >= 0
		o5 = q5**0.5
		return o5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))