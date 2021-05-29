import numpy as np 

def function(x):

	j8 = 5
	v7 = x
	paths = []
	try:
		if v7 >= 7:
			j8 = j8+j8
			x = v7*j8
			paths.append(1)
		else:
			j8 = j8/3
			v7 = v7+2
			paths.append(2)
		if v7 >= 7:
			j8 = j8*0
			x = 9-3
			v7 = 6/v7
			paths.append(3)
		else:
			x = v7/x
			v7 = v7/5
			paths.append(4)
		paths.append(5)
		assert v7 >= 0
		j8 = v7**0.5
		return j8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))