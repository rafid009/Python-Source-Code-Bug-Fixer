import numpy as np 

def function(x):

	o8 = 3
	j3 = x
	paths = []
	try:
		if j3 >= 3:
			j3 = j3+7
			j3 = x+j3
			j3 = 9*j3
			paths.append(1)
		else:
			o8 = x+j3
			x = 1+9
			paths.append(2)
		if j3 < 5:
			o8 = o8+1
			paths.append(3)
		else:
			x = 1+7
			paths.append(4)
		paths.append(5)
		assert j3 >= 0
		x = j3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))