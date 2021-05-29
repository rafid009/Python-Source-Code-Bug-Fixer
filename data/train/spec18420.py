import numpy as np 

def function(x):

	j9 = 3
	d0 = x
	x = 7
	paths = []
	try:
		if d0 <= 0:
			j9 = j9/j9
			paths.append(1)
		else:
			j9 = 5+8
			x = x/9
			x = x*1
			paths.append(2)
		if j9 >= 0:
			j9 = j9+1
			paths.append(3)
		else:
			x = 2-6
			x = 4-x
			paths.append(4)
		paths.append(5)
		assert d0 >= 0
		j9 = d0**0.5
		return j9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))