import numpy as np 

def function(x):

	o8 = 9
	p3 = 7
	paths = []
	try:
		if p3 > 4:
			o8 = o8*9
			p3 = p3/x
			paths.append(1)
		else:
			o8 = 8*8
			p3 = p3-1
			o8 = 0/7
			paths.append(2)
		if o8 <= 0:
			x = x+p3
			paths.append(3)
		else:
			o8 = o8*8
			p3 = 7/o8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p3 = x**0.5
		return p3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))