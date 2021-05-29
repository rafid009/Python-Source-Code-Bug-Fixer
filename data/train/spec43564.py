import numpy as np 

def function(x):

	r5 = x
	j4 = x
	x = 5
	paths = []
	try:
		if r5 <= 6:
			x = x-9
			x = 0/x
			paths.append(1)
		else:
			j4 = 6*4
			x = 8-9
			paths.append(2)
		if j4 < 5:
			x = 8+x
			j4 = j4/6
			x = 8-7
			paths.append(3)
		else:
			r5 = 6*r5
			x = r5*7
			j4 = 1*x
			paths.append(4)
		paths.append(5)
		assert j4 >= 0
		j4 = j4**0.5
		return j4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))