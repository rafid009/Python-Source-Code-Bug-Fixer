import numpy as np 

def function(x):

	o8 = 5
	p9 = x
	paths = []
	try:
		if p9 < 0:
			o8 = o8/7
			p9 = 2*7
			paths.append(1)
		else:
			x = 6/x
			o8 = o8*5
			p9 = p9/5
			paths.append(2)
		if p9 >= 4:
			o8 = o8*0
			paths.append(3)
		else:
			p9 = p9-x
			x = 5*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p9 = x**0.5
		return p9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))