import numpy as np 

def function(x):

	d0 = x
	q5 = 4
	paths = []
	try:
		if q5 >= 4:
			x = x-9
			q5 = x+d0
			paths.append(1)
		else:
			d0 = 3/8
			paths.append(2)
		if d0 > 3:
			x = 2+x
			paths.append(3)
		else:
			x = x-6
			x = x-2
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