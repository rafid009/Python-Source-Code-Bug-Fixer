import numpy as np 

def function(x):

	a7 = x
	o1 = 8
	paths = []
	try:
		if x > 8:
			o1 = 3*0
			paths.append(1)
		else:
			o1 = o1*x
			x = a7*7
			o1 = o1+o1
			paths.append(2)
		if a7 < 8:
			x = x*a7
			paths.append(3)
		else:
			a7 = 3+2
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