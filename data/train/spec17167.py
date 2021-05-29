import numpy as np 

def function(x):

	q5 = x
	d0 = 0
	paths = []
	try:
		if q5 > 7:
			q5 = 5*q5
			paths.append(1)
		else:
			d0 = 6*4
			q5 = q5+4
			x = x*0
			paths.append(2)
		if q5 > 2:
			x = 0+x
			d0 = 6/q5
			d0 = 5-7
			paths.append(3)
		else:
			d0 = d0/8
			x = x+4
			x = x+x
			paths.append(4)
		paths.append(5)
		assert q5 >= 0
		x = q5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))