import numpy as np 

def function(x):

	d8 = x
	j3 = x
	paths = []
	try:
		if d8 <= 3:
			d8 = d8+3
			x = 3-9
			paths.append(1)
		else:
			d8 = 2-7
			j3 = j3+3
			d8 = x/j3
			paths.append(2)
		if d8 > 7:
			x = d8-0
			x = 6-x
			paths.append(3)
		else:
			x = 9*4
			paths.append(4)
		paths.append(5)
		assert d8 >= 0
		j3 = d8**0.5
		return j3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))