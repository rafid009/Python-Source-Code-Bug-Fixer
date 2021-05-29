import numpy as np 

def function(x):

	i2 = x
	r9 = 0
	paths = []
	try:
		if r9 < 7:
			i2 = i2+5
			i2 = 4/i2
			r9 = r9+6
			paths.append(1)
		else:
			r9 = r9*5
			i2 = 5*i2
			i2 = i2+x
			paths.append(2)
		if r9 > 2:
			r9 = r9*1
			paths.append(3)
		else:
			r9 = r9/i2
			r9 = r9/r9
			i2 = r9-i2
			paths.append(4)
		paths.append(5)
		assert i2 >= 0
		r9 = i2**0.5
		return r9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))