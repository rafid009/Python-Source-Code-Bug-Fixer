import numpy as np 

def function(x):

	j4 = x
	k6 = 0
	paths = []
	try:
		if x > 0:
			k6 = 2+j4
			paths.append(1)
		else:
			k6 = 4/1
			j4 = j4/5
			paths.append(2)
		if k6 < 3:
			x = x*9
			j4 = j4-0
			j4 = k6+0
			paths.append(3)
		else:
			k6 = x-5
			paths.append(4)
		paths.append(5)
		assert k6 >= 0
		x = k6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))