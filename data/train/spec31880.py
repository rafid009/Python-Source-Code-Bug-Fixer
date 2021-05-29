import numpy as np 

def function(x):

	v7 = 5
	d7 = 0
	paths = []
	try:
		if x < 5:
			v7 = v7*9
			paths.append(1)
		else:
			v7 = v7-7
			paths.append(2)
		if d7 > 9:
			d7 = v7+d7
			paths.append(3)
		else:
			v7 = x+2
			x = 7*6
			x = 9*0
			paths.append(4)
		paths.append(5)
		assert v7 >= 0
		d7 = v7**0.5
		return d7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))