import numpy as np 

def function(x):

	d1 = 5
	b9 = 0
	paths = []
	try:
		if b9 < 9:
			x = x/5
			b9 = 0/3
			b9 = 9-6
			paths.append(1)
		else:
			x = x/2
			b9 = b9/2
			paths.append(2)
		if d1 > 5:
			x = 3/7
			b9 = 7/d1
			d1 = d1+8
			paths.append(3)
		else:
			d1 = x*d1
			x = x*9
			paths.append(4)
		paths.append(5)
		assert d1 >= 0
		x = d1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))