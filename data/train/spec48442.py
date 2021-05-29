import numpy as np 

def function(x):

	u4 = 6
	j5 = x
	paths = []
	try:
		if x > 5:
			u4 = j5+x
			j5 = u4/j5
			paths.append(1)
		else:
			j5 = u4*2
			u4 = 0+u4
			paths.append(2)
		if u4 >= 7:
			u4 = x*u4
			paths.append(3)
		else:
			j5 = x/u4
			j5 = 1*j5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j5 = x**0.5
		return j5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))