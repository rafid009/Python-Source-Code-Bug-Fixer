import numpy as np 

def function(x):

	v5 = 9
	d8 = x
	paths = []
	try:
		if d8 > 6:
			x = 2-x
			d8 = 2+d8
			paths.append(1)
		else:
			v5 = d8*9
			paths.append(2)
		if d8 < 8:
			x = x-v5
			x = 8/x
			paths.append(3)
		else:
			x = d8*0
			v5 = x/v5
			d8 = v5*d8
			paths.append(4)
		paths.append(5)
		assert d8 >= 0
		v5 = d8**0.5
		return v5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))