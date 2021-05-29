import numpy as np 

def function(x):

	e7 = 8
	o1 = x
	paths = []
	try:
		if e7 > 3:
			x = 3*2
			e7 = e7*5
			paths.append(1)
		else:
			e7 = e7/8
			e7 = x/e7
			paths.append(2)
		if o1 <= 2:
			e7 = 5*o1
			o1 = o1/8
			e7 = e7+9
			paths.append(3)
		else:
			o1 = 2/o1
			paths.append(4)
		paths.append(5)
		assert o1 >= 0
		o1 = o1**0.5
		return o1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))