import numpy as np 

def function(x):

	j5 = 6
	u6 = x
	paths = []
	try:
		if u6 < 7:
			x = x*5
			j5 = 6-j5
			u6 = 3-3
			paths.append(1)
		else:
			u6 = 7/7
			paths.append(2)
		if x > 8:
			u6 = u6*0
			x = 2+x
			paths.append(3)
		else:
			j5 = 8*j5
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