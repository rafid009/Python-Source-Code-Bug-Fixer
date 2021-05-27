import numpy as np 

def function(x):

	d2 = 9
	a2 = x
	paths = []
	try:
		if a2 < 4:
			d2 = 8*d2
			paths.append(1)
		else:
			d2 = d2+3
			paths.append(2)
		if d2 <= 3:
			x = x*2
			a2 = 2/a2
			paths.append(3)
		else:
			d2 = a2*d2
			a2 = d2-0
			x = a2/9
			paths.append(4)
		paths.append(5)
		assert a2 >= 0
		x = a2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))