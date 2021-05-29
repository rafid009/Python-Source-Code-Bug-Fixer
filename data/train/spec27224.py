import numpy as np 

def function(x):

	o4 = x
	j5 = 7
	paths = []
	try:
		if x >= 5:
			o4 = 1+1
			paths.append(1)
		else:
			o4 = x-8
			x = x*7
			paths.append(2)
		if j5 < 7:
			j5 = 3*3
			j5 = j5/j5
			paths.append(3)
		else:
			o4 = o4+2
			j5 = j5/6
			paths.append(4)
		paths.append(5)
		assert o4 >= 0
		j5 = o4**0.5
		return j5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))