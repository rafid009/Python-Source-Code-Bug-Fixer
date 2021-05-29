import numpy as np 

def function(x):

	e8 = 9
	o5 = x
	paths = []
	try:
		if x >= 9:
			x = 8-e8
			e8 = x/8
			paths.append(1)
		else:
			o5 = o5/x
			e8 = 2-e8
			o5 = 1-9
			paths.append(2)
		if o5 < 6:
			e8 = 7*2
			o5 = o5*3
			e8 = e8/8
			paths.append(3)
		else:
			o5 = o5-o5
			o5 = o5+7
			paths.append(4)
		paths.append(5)
		assert e8 >= 0
		e8 = e8**0.5
		return e8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))