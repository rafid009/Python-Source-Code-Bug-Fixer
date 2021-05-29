import numpy as np 

def function(x):

	o2 = 7
	p3 = 4
	paths = []
	try:
		if x < 8:
			o2 = o2/o2
			paths.append(1)
		else:
			p3 = p3*7
			o2 = x/o2
			x = 0-x
			paths.append(2)
		if p3 >= 9:
			p3 = 4-8
			o2 = o2+8
			p3 = 7+p3
			paths.append(3)
		else:
			p3 = p3+x
			o2 = p3*1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o2 = x**0.5
		return o2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))