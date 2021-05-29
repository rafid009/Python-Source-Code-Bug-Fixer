import numpy as np 

def function(x):

	v1 = 0
	d4 = x
	paths = []
	try:
		if v1 >= 9:
			x = x*1
			d4 = d4*6
			d4 = d4/1
			paths.append(1)
		else:
			d4 = d4*3
			d4 = x+d4
			paths.append(2)
		if v1 >= 4:
			x = 5-x
			x = v1*x
			v1 = v1*3
			paths.append(3)
		else:
			v1 = 4*1
			v1 = x/v1
			paths.append(4)
		paths.append(5)
		assert v1 >= 0
		d4 = v1**0.5
		return d4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))