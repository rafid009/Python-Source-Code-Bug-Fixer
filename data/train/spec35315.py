import numpy as np 

def function(x):

	d2 = x
	j5 = 5
	paths = []
	try:
		if j5 <= 4:
			j5 = j5-7
			paths.append(1)
		else:
			d2 = 1+d2
			j5 = 2-j5
			paths.append(2)
		if x > 8:
			d2 = d2/2
			x = x*d2
			j5 = 9-j5
			paths.append(3)
		else:
			j5 = j5*9
			paths.append(4)
		paths.append(5)
		assert d2 >= 0
		x = d2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))