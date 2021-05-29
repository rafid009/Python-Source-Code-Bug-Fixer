import numpy as np 

def function(x):

	j8 = 9
	v5 = x
	paths = []
	try:
		if x > 7:
			j8 = v5-j8
			x = j8*3
			x = x*1
			paths.append(1)
		else:
			x = 3/j8
			paths.append(2)
		if j8 >= 8:
			x = 7*1
			paths.append(3)
		else:
			v5 = v5/x
			j8 = v5*6
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