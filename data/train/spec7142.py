import numpy as np 

def function(x):

	x6 = 9
	j3 = x
	paths = []
	try:
		if x6 <= 2:
			x6 = x6+x6
			j3 = 8*7
			x = x*x
			paths.append(1)
		else:
			x = j3+x
			x = x*9
			j3 = x-x
			paths.append(2)
		if j3 < 8:
			j3 = 7*1
			paths.append(3)
		else:
			j3 = 9/j3
			x6 = x6*7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j3 = x**0.5
		return j3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))