import numpy as np 

def function(x):

	y0 = x
	i5 = 1
	paths = []
	try:
		if x >= 3:
			i5 = i5*i5
			y0 = y0/7
			y0 = i5-y0
			paths.append(1)
		else:
			x = x*0
			x = 7*3
			i5 = i5+i5
			paths.append(2)
		if i5 < 7:
			i5 = y0-i5
			y0 = y0*y0
			paths.append(3)
		else:
			y0 = y0-0
			x = 7+x
			paths.append(4)
		paths.append(5)
		assert i5 >= 0
		x = i5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))