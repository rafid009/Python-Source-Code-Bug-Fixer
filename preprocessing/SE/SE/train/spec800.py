import numpy as np 

def function(x):

	o5 = 6
	e5 = x
	x = x
	paths = []
	try:
		if x < 6:
			e5 = o5*2
			x = e5/x
			paths.append(1)
		else:
			o5 = e5*o5
			paths.append(2)
		if x <= 3:
			x = 9+5
			o5 = o5*4
			x = x*4
			paths.append(3)
		else:
			o5 = o5-9
			e5 = e5/8
			x = 4/7
			paths.append(4)
		paths.append(5)
		assert o5 >= 0
		e5 = o5**0.5
		return e5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))