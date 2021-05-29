import numpy as np 

def function(x):

	j8 = x
	d1 = 9
	paths = []
	try:
		if j8 > 5:
			d1 = d1-0
			x = 4*2
			paths.append(1)
		else:
			d1 = 0-1
			j8 = j8-x
			j8 = j8*1
			paths.append(2)
		if d1 < 8:
			x = x*d1
			x = x/x
			paths.append(3)
		else:
			x = 5+x
			paths.append(4)
		paths.append(5)
		assert d1 >= 0
		d1 = d1**0.5
		return d1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))