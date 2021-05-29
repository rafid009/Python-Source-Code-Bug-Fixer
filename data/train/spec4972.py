import numpy as np 

def function(x):

	d4 = 7
	j7 = x
	paths = []
	try:
		if d4 <= 5:
			j7 = 1-j7
			d4 = d4/9
			paths.append(1)
		else:
			x = x-x
			paths.append(2)
		if j7 <= 9:
			j7 = 0*d4
			j7 = 6*0
			paths.append(3)
		else:
			d4 = d4-9
			x = 5+x
			j7 = 3*j7
			paths.append(4)
		paths.append(5)
		assert d4 >= 0
		j7 = d4**0.5
		return j7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))