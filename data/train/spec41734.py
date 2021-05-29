import numpy as np 

def function(x):

	a9 = x
	o7 = x
	paths = []
	try:
		if a9 <= 7:
			a9 = o7*x
			paths.append(1)
		else:
			o7 = x/1
			a9 = x/7
			o7 = o7*0
			paths.append(2)
		if o7 <= 8:
			o7 = 2*2
			x = o7+x
			o7 = o7*1
			paths.append(3)
		else:
			x = o7-8
			o7 = 6-o7
			a9 = a9-7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))