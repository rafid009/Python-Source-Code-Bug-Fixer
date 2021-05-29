import numpy as np 

def function(x):

	o1 = x
	a6 = 1
	paths = []
	try:
		if x > 1:
			x = 7/6
			o1 = 6-5
			o1 = 4-2
			paths.append(1)
		else:
			o1 = o1+o1
			a6 = 1-a6
			paths.append(2)
		if a6 <= 5:
			x = x+x
			o1 = o1*2
			o1 = 5-o1
			paths.append(3)
		else:
			x = x+5
			o1 = o1/8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a6 = x**0.5
		return a6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))