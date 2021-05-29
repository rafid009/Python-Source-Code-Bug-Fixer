import numpy as np 

def function(x):

	o9 = x
	e1 = 4
	paths = []
	try:
		if o9 >= 1:
			x = x*4
			o9 = o9+1
			paths.append(1)
		else:
			o9 = o9*e1
			x = 7+x
			paths.append(2)
		if e1 <= 7:
			o9 = 3*o9
			paths.append(3)
		else:
			x = e1+x
			paths.append(4)
		paths.append(5)
		assert o9 >= 0
		o9 = o9**0.5
		return o9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))