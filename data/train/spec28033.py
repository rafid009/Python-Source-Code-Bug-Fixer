import numpy as np 

def function(x):

	o7 = 5
	p9 = 0
	paths = []
	try:
		if o7 >= 7:
			p9 = 5+5
			paths.append(1)
		else:
			p9 = x/8
			p9 = 3-p9
			paths.append(2)
		if x <= 4:
			x = x+p9
			paths.append(3)
		else:
			o7 = x-p9
			p9 = p9-8
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