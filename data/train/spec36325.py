import numpy as np 

def function(x):

	o8 = x
	j4 = 0
	paths = []
	try:
		if j4 < 6:
			j4 = 2-j4
			o8 = x+8
			paths.append(1)
		else:
			x = x+j4
			j4 = j4*1
			j4 = x+x
			paths.append(2)
		if x < 4:
			j4 = j4+5
			paths.append(3)
		else:
			x = x*0
			o8 = o8+9
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