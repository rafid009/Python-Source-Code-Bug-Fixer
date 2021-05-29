import numpy as np 

def function(x):

	d5 = 1
	e4 = x
	paths = []
	try:
		if d5 > 7:
			d5 = d5*1
			e4 = e4-d5
			paths.append(1)
		else:
			x = 5*3
			e4 = 1+e4
			e4 = 1*e4
			paths.append(2)
		if x > 2:
			e4 = e4+d5
			x = x*7
			d5 = d5+1
			paths.append(3)
		else:
			e4 = e4+x
			e4 = 5+2
			d5 = d5/x
			paths.append(4)
		paths.append(5)
		assert e4 >= 0
		e4 = e4**0.5
		return e4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))