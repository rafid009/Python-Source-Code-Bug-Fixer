import numpy as np 

def function(x):

	o5 = 2
	a0 = x
	paths = []
	try:
		if x > 1:
			o5 = o5+x
			a0 = 9*a0
			paths.append(1)
		else:
			o5 = 5/1
			x = 1*8
			paths.append(2)
		if a0 < 5:
			a0 = a0*5
			a0 = a0+9
			a0 = a0/x
			paths.append(3)
		else:
			o5 = o5/6
			a0 = a0/a0
			x = 3*x
			paths.append(4)
		paths.append(5)
		assert a0 >= 0
		o5 = a0**0.5
		return o5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))