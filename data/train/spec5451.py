import numpy as np 

def function(x):

	d2 = x
	q2 = 0
	paths = []
	try:
		if x >= 3:
			d2 = d2/2
			d2 = 7*1
			x = x-8
			paths.append(1)
		else:
			x = x+x
			x = x+q2
			paths.append(2)
		if q2 < 4:
			x = d2+d2
			q2 = q2*d2
			q2 = 7/x
			paths.append(3)
		else:
			d2 = d2*8
			d2 = d2/q2
			paths.append(4)
		paths.append(5)
		assert q2 >= 0
		x = q2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))