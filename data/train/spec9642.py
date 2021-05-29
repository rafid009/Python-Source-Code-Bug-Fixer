import numpy as np 

def function(x):

	d8 = 4
	b9 = 1
	paths = []
	try:
		if d8 > 8:
			b9 = b9+0
			d8 = d8-1
			d8 = d8*2
			paths.append(1)
		else:
			x = d8+x
			b9 = x+6
			paths.append(2)
		if b9 <= 4:
			d8 = x-d8
			b9 = 5*b9
			paths.append(3)
		else:
			d8 = d8*d8
			b9 = 7+8
			paths.append(4)
		paths.append(5)
		assert b9 >= 0
		d8 = b9**0.5
		return d8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))