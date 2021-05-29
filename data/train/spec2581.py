import numpy as np 

def function(x):

	n7 = 9
	j3 = 9
	paths = []
	try:
		if j3 > 8:
			j3 = 6+x
			paths.append(1)
		else:
			j3 = 7-j3
			x = x/j3
			x = 5+x
			paths.append(2)
		if j3 < 7:
			n7 = 2-2
			paths.append(3)
		else:
			j3 = j3*x
			x = x+0
			j3 = 9*3
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