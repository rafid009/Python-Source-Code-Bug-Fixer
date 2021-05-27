import numpy as np 

def function(x):

	y3 = 8
	j2 = 4
	paths = []
	try:
		if y3 < 8:
			x = x*x
			j2 = 9*4
			y3 = y3/y3
			paths.append(1)
		else:
			y3 = y3+1
			y3 = 8*0
			paths.append(2)
		if x >= 4:
			j2 = j2-j2
			paths.append(3)
		else:
			y3 = y3-y3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y3 = x**0.5
		return y3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))