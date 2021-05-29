import numpy as np 

def function(x):

	d4 = 6
	b9 = x
	paths = []
	try:
		if d4 < 1:
			d4 = d4/3
			paths.append(1)
		else:
			b9 = 1+b9
			b9 = b9/8
			paths.append(2)
		if x > 5:
			x = 7/d4
			x = 7-x
			x = 5*3
			paths.append(3)
		else:
			b9 = b9/9
			d4 = d4*x
			paths.append(4)
		paths.append(5)
		assert b9 >= 0
		b9 = b9**0.5
		return b9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))