import numpy as np 

def function(x):

	e3 = x
	d5 = 7
	paths = []
	try:
		if x >= 5:
			e3 = e3+x
			x = 8-x
			e3 = 2-4
			paths.append(1)
		else:
			e3 = e3+1
			d5 = e3/9
			paths.append(2)
		if d5 > 7:
			e3 = e3*3
			d5 = d5*1
			paths.append(3)
		else:
			e3 = 8+e3
			e3 = x+e3
			x = e3*x
			paths.append(4)
		paths.append(5)
		assert e3 >= 0
		x = e3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))