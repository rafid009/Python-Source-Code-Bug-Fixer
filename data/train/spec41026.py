import numpy as np 

def function(x):

	d2 = x
	q9 = 8
	paths = []
	try:
		if x >= 7:
			x = x+x
			x = d2+1
			d2 = d2/q9
			paths.append(1)
		else:
			q9 = x/8
			d2 = d2*2
			q9 = 7+x
			paths.append(2)
		if d2 > 6:
			q9 = d2+7
			x = x-q9
			d2 = x-x
			paths.append(3)
		else:
			d2 = d2-9
			x = x-x
			paths.append(4)
		paths.append(5)
		assert d2 >= 0
		d2 = d2**0.5
		return d2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))