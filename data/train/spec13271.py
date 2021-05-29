import numpy as np 

def function(x):

	f1 = 4
	d6 = 6
	x = x
	paths = []
	try:
		if x < 5:
			f1 = f1-5
			d6 = d6+8
			paths.append(1)
		else:
			f1 = 8-x
			f1 = f1-f1
			paths.append(2)
		if f1 > 0:
			f1 = f1+9
			x = 1-5
			d6 = d6+x
			paths.append(3)
		else:
			d6 = 8*x
			f1 = 1/9
			paths.append(4)
		paths.append(5)
		assert d6 >= 0
		d6 = d6**0.5
		return d6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))