import numpy as np 

def function(x):

	o1 = x
	j4 = x
	paths = []
	try:
		if x < 8:
			j4 = 6/j4
			o1 = x/5
			x = x*5
			paths.append(1)
		else:
			x = o1-7
			o1 = 0*o1
			x = o1*1
			paths.append(2)
		if o1 < 7:
			j4 = j4+x
			j4 = 3*j4
			j4 = j4+x
			paths.append(3)
		else:
			o1 = 3*o1
			x = 5-8
			o1 = j4-j4
			paths.append(4)
		paths.append(5)
		assert j4 >= 0
		x = j4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))