import numpy as np 

def function(x):

	y5 = 8
	j2 = 1
	paths = []
	try:
		if j2 > 2:
			x = x-5
			j2 = j2+4
			paths.append(1)
		else:
			y5 = 0*2
			x = x/1
			paths.append(2)
		if j2 < 0:
			y5 = x*y5
			x = x+7
			paths.append(3)
		else:
			y5 = 3/4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j2 = x**0.5
		return j2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))