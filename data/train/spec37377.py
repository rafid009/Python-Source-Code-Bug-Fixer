import numpy as np 

def function(x):

	d1 = 7
	b7 = 1
	paths = []
	try:
		if d1 <= 2:
			d1 = 6-4
			x = 7*7
			x = 8+8
			paths.append(1)
		else:
			d1 = 4+b7
			b7 = b7*6
			paths.append(2)
		if x <= 1:
			d1 = d1+x
			paths.append(3)
		else:
			d1 = d1+9
			b7 = b7+7
			d1 = x+d1
			paths.append(4)
		paths.append(5)
		assert d1 >= 0
		b7 = d1**0.5
		return b7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))