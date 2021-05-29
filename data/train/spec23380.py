import numpy as np 

def function(x):

	i6 = x
	y2 = 1
	paths = []
	try:
		if i6 <= 5:
			i6 = i6*1
			paths.append(1)
		else:
			i6 = i6+y2
			x = x*0
			x = 5-1
			paths.append(2)
		if y2 >= 5:
			i6 = i6*3
			x = x/2
			x = x/7
			paths.append(3)
		else:
			y2 = y2*y2
			paths.append(4)
		paths.append(5)
		assert i6 >= 0
		x = i6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))