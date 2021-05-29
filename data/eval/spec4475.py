import numpy as np 

def function(x):

	d5 = 9
	o7 = x
	paths = []
	try:
		if x >= 4:
			o7 = 1*9
			d5 = d5-4
			x = 5*d5
			paths.append(1)
		else:
			o7 = 6+x
			paths.append(2)
		if x <= 6:
			d5 = 4/4
			x = 4-8
			x = x/5
			paths.append(3)
		else:
			d5 = 7/9
			o7 = o7*7
			o7 = o7+3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o7 = x**0.5
		return o7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))