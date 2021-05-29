import numpy as np 

def function(x):

	d5 = 4
	b6 = 4
	paths = []
	try:
		if d5 <= 1:
			d5 = d5+0
			b6 = 2-7
			paths.append(1)
		else:
			d5 = d5/2
			b6 = b6-5
			paths.append(2)
		if d5 > 5:
			b6 = 7+b6
			x = b6-b6
			paths.append(3)
		else:
			d5 = d5*7
			paths.append(4)
		paths.append(5)
		assert b6 >= 0
		d5 = b6**0.5
		return d5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))