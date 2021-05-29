import numpy as np 

def function(x):

	x3 = x
	j4 = 4
	paths = []
	try:
		if j4 < 3:
			x = x*2
			j4 = j4*0
			paths.append(1)
		else:
			x3 = 7+x3
			x = x-8
			j4 = j4/8
			paths.append(2)
		if x3 >= 5:
			j4 = 3-j4
			x3 = 0+x
			j4 = j4-5
			paths.append(3)
		else:
			x = 9-x
			j4 = j4-7
			paths.append(4)
		paths.append(5)
		assert x3 >= 0
		x3 = x3**0.5
		return x3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))