import numpy as np 

def function(x):

	j2 = x
	d2 = x
	paths = []
	try:
		if d2 <= 0:
			d2 = 5*9
			paths.append(1)
		else:
			x = 1+0
			x = x*x
			paths.append(2)
		if j2 < 0:
			d2 = d2-1
			paths.append(3)
		else:
			d2 = 2+d2
			paths.append(4)
		paths.append(5)
		assert j2 >= 0
		x = j2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))