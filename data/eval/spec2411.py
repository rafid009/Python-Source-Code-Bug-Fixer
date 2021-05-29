import numpy as np 

def function(x):

	o0 = 8
	e9 = x
	paths = []
	try:
		if x <= 6:
			x = x*5
			x = x+e9
			paths.append(1)
		else:
			o0 = o0-o0
			e9 = e9*o0
			paths.append(2)
		if e9 < 3:
			x = e9*e9
			e9 = 8-e9
			e9 = 1-e9
			paths.append(3)
		else:
			o0 = o0+x
			o0 = e9*8
			x = 9-x
			paths.append(4)
		paths.append(5)
		assert e9 >= 0
		e9 = e9**0.5
		return e9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))