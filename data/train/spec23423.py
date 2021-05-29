import numpy as np 

def function(x):

	j8 = x
	x2 = 2
	paths = []
	try:
		if j8 >= 5:
			x = 6+1
			j8 = j8-1
			j8 = 4/j8
			paths.append(1)
		else:
			x = x*3
			x2 = x2-5
			x = 6+j8
			paths.append(2)
		if j8 < 9:
			j8 = j8+x
			paths.append(3)
		else:
			x2 = x2/x2
			paths.append(4)
		paths.append(5)
		assert j8 >= 0
		j8 = j8**0.5
		return j8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))