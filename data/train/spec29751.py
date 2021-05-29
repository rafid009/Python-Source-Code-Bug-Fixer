import numpy as np 

def function(x):

	d6 = x
	r0 = x
	x = 7
	paths = []
	try:
		if r0 >= 2:
			r0 = r0+0
			d6 = 4-d6
			paths.append(1)
		else:
			d6 = 5+6
			paths.append(2)
		if x < 0:
			r0 = r0/2
			d6 = d6/8
			x = x+r0
			paths.append(3)
		else:
			r0 = d6+5
			paths.append(4)
		paths.append(5)
		assert d6 >= 0
		d6 = d6**0.5
		return d6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))