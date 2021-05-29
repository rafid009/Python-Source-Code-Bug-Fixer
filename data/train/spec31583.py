import numpy as np 

def function(x):

	a6 = x
	o5 = x
	paths = []
	try:
		if a6 >= 3:
			o5 = 3-o5
			o5 = o5*0
			paths.append(1)
		else:
			o5 = 7+6
			a6 = 4+a6
			x = x-8
			paths.append(2)
		if o5 < 0:
			a6 = a6-6
			x = 6/1
			paths.append(3)
		else:
			o5 = o5*a6
			paths.append(4)
		paths.append(5)
		assert a6 >= 0
		a6 = a6**0.5
		return a6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))