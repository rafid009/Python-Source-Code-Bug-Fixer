import numpy as np 

def function(x):

	d0 = x
	v7 = 6
	paths = []
	try:
		if v7 <= 8:
			d0 = d0+7
			v7 = x+7
			paths.append(1)
		else:
			x = x-8
			d0 = x/d0
			paths.append(2)
		if x > 8:
			v7 = 4/1
			v7 = v7-5
			paths.append(3)
		else:
			x = 3-x
			x = 7+x
			d0 = v7-7
			paths.append(4)
		paths.append(5)
		assert v7 >= 0
		v7 = v7**0.5
		return v7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))