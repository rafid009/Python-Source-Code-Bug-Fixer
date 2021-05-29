import numpy as np 

def function(x):

	b0 = x
	d7 = 6
	paths = []
	try:
		if b0 > 1:
			x = x/8
			b0 = b0-9
			x = x+x
			paths.append(1)
		else:
			x = b0+1
			paths.append(2)
		if d7 <= 4:
			x = 6/3
			b0 = 1*7
			d7 = d7+1
			paths.append(3)
		else:
			x = x*5
			paths.append(4)
		paths.append(5)
		assert b0 >= 0
		x = b0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))