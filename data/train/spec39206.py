import numpy as np 

def function(x):

	x6 = x
	v5 = 9
	paths = []
	try:
		if v5 >= 8:
			x6 = x6/v5
			paths.append(1)
		else:
			x = 5-x
			v5 = 5-v5
			v5 = x6*9
			paths.append(2)
		if x6 > 4:
			x = 7*1
			x = 2-x
			x6 = x6*0
			paths.append(3)
		else:
			v5 = 7+v5
			paths.append(4)
		paths.append(5)
		assert x6 >= 0
		x = x6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))