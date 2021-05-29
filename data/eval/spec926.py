import numpy as np 

def function(x):

	m1 = x
	d5 = x
	paths = []
	try:
		if x <= 1:
			d5 = m1*d5
			d5 = 2/d5
			paths.append(1)
		else:
			m1 = 6-d5
			paths.append(2)
		if d5 <= 1:
			m1 = m1+x
			x = x-d5
			paths.append(3)
		else:
			x = 7/9
			x = x*7
			paths.append(4)
		paths.append(5)
		assert m1 >= 0
		d5 = m1**0.5
		return d5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))