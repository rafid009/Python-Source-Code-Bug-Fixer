import numpy as np 

def function(x):

	d2 = x
	i5 = 6
	paths = []
	try:
		if d2 <= 7:
			i5 = i5*2
			x = x*3
			paths.append(1)
		else:
			d2 = d2*i5
			paths.append(2)
		if d2 < 3:
			d2 = x+d2
			paths.append(3)
		else:
			i5 = i5*d2
			d2 = d2*8
			paths.append(4)
		paths.append(5)
		assert d2 >= 0
		d2 = d2**0.5
		return d2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))