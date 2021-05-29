import numpy as np 

def function(x):

	n3 = 6
	j5 = x
	x = x
	paths = []
	try:
		if j5 <= 6:
			n3 = 9*1
			j5 = j5/7
			paths.append(1)
		else:
			x = x-9
			x = 8/4
			paths.append(2)
		if x > 3:
			j5 = x-7
			j5 = j5-x
			x = x*x
			paths.append(3)
		else:
			n3 = 5+x
			j5 = j5/6
			n3 = j5*j5
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