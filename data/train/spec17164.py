import numpy as np 

def function(x):

	v1 = 9
	d9 = 6
	paths = []
	try:
		if x < 2:
			x = 8-x
			x = v1-5
			paths.append(1)
		else:
			v1 = v1*3
			paths.append(2)
		if v1 < 8:
			d9 = x*0
			v1 = 7*2
			paths.append(3)
		else:
			v1 = 5+2
			v1 = 0/2
			x = x-8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d9 = x**0.5
		return d9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))