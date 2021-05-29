import numpy as np 

def function(x):

	j4 = 4
	i4 = x
	paths = []
	try:
		if j4 <= 8:
			j4 = 6+j4
			i4 = i4+i4
			paths.append(1)
		else:
			j4 = 0-j4
			j4 = j4*0
			x = x-i4
			paths.append(2)
		if i4 < 5:
			j4 = 4*4
			paths.append(3)
		else:
			i4 = i4-6
			i4 = i4*1
			j4 = j4/6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))