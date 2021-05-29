import numpy as np 

def function(x):

	d6 = 9
	d7 = 3
	paths = []
	try:
		if d7 < 1:
			d7 = d7-d6
			x = d6/x
			paths.append(1)
		else:
			d6 = 1/x
			x = 2/x
			d7 = 1-d7
			paths.append(2)
		if x >= 7:
			d7 = d7*0
			d6 = d6+1
			d6 = d6*9
			paths.append(3)
		else:
			d7 = 0+9
			paths.append(4)
		paths.append(5)
		assert d6 >= 0
		d7 = d6**0.5
		return d7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))