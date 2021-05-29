import numpy as np 

def function(x):

	j9 = 8
	e6 = x
	paths = []
	try:
		if j9 <= 1:
			j9 = j9*9
			j9 = e6/9
			paths.append(1)
		else:
			e6 = e6/j9
			e6 = 5+e6
			paths.append(2)
		if e6 < 2:
			x = x+j9
			x = x*4
			j9 = e6-7
			paths.append(3)
		else:
			x = x+j9
			j9 = x-j9
			paths.append(4)
		paths.append(5)
		assert e6 >= 0
		j9 = e6**0.5
		return j9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))