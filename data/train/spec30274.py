import numpy as np 

def function(x):

	i2 = 1
	d9 = x
	x = 3
	paths = []
	try:
		if d9 <= 7:
			x = x*d9
			x = x+1
			paths.append(1)
		else:
			d9 = 9+d9
			x = x/x
			i2 = i2+2
			paths.append(2)
		if d9 <= 6:
			x = i2*i2
			x = x/i2
			i2 = i2*x
			paths.append(3)
		else:
			i2 = i2-2
			d9 = d9+6
			x = 5+2
			paths.append(4)
		paths.append(5)
		assert i2 >= 0
		x = i2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))