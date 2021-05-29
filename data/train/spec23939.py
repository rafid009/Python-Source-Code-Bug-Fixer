import numpy as np 

def function(x):

	j3 = x
	d5 = 1
	paths = []
	try:
		if d5 >= 1:
			d5 = 9/x
			j3 = 3/x
			paths.append(1)
		else:
			d5 = 6-d5
			j3 = j3+x
			d5 = d5/8
			paths.append(2)
		if x < 9:
			j3 = j3-7
			j3 = 6+7
			paths.append(3)
		else:
			x = x+1
			j3 = 5-1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d5 = x**0.5
		return d5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))