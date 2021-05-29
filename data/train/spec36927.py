import numpy as np 

def function(x):

	d2 = 2
	q5 = x
	paths = []
	try:
		if d2 <= 8:
			x = x*q5
			paths.append(1)
		else:
			q5 = q5-2
			d2 = d2/q5
			paths.append(2)
		if x >= 3:
			x = x/x
			d2 = d2+0
			q5 = q5*4
			paths.append(3)
		else:
			d2 = 6+d2
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