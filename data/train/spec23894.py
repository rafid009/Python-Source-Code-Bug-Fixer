import numpy as np 

def function(x):

	y2 = x
	v6 = x
	paths = []
	try:
		if x > 9:
			v6 = 3+x
			x = x*9
			paths.append(1)
		else:
			v6 = v6+1
			y2 = y2+x
			y2 = v6+y2
			paths.append(2)
		if y2 >= 6:
			v6 = y2+2
			y2 = y2*1
			y2 = 6-y2
			paths.append(3)
		else:
			y2 = y2-7
			v6 = 3/6
			paths.append(4)
		paths.append(5)
		assert y2 >= 0
		x = y2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))