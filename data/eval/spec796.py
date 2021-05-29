import numpy as np 

def function(x):

	d0 = 0
	q5 = x
	paths = []
	try:
		if q5 > 0:
			q5 = x+d0
			x = x*0
			paths.append(1)
		else:
			q5 = q5-x
			d0 = d0/8
			d0 = 1+d0
			paths.append(2)
		if d0 > 1:
			d0 = d0*2
			d0 = d0/q5
			paths.append(3)
		else:
			q5 = 9*q5
			d0 = 0-6
			d0 = 3/d0
			paths.append(4)
		paths.append(5)
		assert d0 >= 0
		d0 = d0**0.5
		return d0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))