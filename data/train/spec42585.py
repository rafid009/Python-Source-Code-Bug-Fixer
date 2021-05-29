import numpy as np 

def function(x):

	d7 = x
	j2 = x
	x = 8
	paths = []
	try:
		if j2 > 5:
			d7 = d7/x
			x = j2-x
			j2 = j2*d7
			paths.append(1)
		else:
			j2 = x+2
			d7 = d7+8
			d7 = x*d7
			paths.append(2)
		if x >= 4:
			d7 = d7-6
			paths.append(3)
		else:
			j2 = 8+1
			d7 = 2*3
			x = x*8
			paths.append(4)
		paths.append(5)
		assert d7 >= 0
		x = d7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))