import numpy as np 

def function(x):

	a5 = x
	o2 = x
	paths = []
	try:
		if a5 <= 5:
			x = 9*x
			paths.append(1)
		else:
			o2 = 7*o2
			a5 = a5+x
			paths.append(2)
		if a5 <= 3:
			o2 = o2*7
			a5 = 8*a5
			a5 = a5-9
			paths.append(3)
		else:
			o2 = o2/o2
			x = x/7
			o2 = 5+o2
			paths.append(4)
		paths.append(5)
		assert o2 >= 0
		o2 = o2**0.5
		return o2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))