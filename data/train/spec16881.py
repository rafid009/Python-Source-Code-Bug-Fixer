import numpy as np 

def function(x):

	i7 = 5
	j8 = x
	paths = []
	try:
		if j8 > 0:
			x = x+8
			i7 = 7-4
			paths.append(1)
		else:
			x = x+3
			x = i7-x
			i7 = i7*0
			paths.append(2)
		if i7 > 4:
			i7 = i7-x
			i7 = x+j8
			paths.append(3)
		else:
			i7 = i7+7
			paths.append(4)
		paths.append(5)
		assert j8 >= 0
		x = j8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))