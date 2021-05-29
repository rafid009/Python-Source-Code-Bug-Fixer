import numpy as np 

def function(x):

	h4 = x
	j8 = x
	paths = []
	try:
		if h4 <= 7:
			j8 = j8*x
			j8 = h4*3
			j8 = 8+j8
			paths.append(1)
		else:
			x = x*2
			h4 = 6-j8
			j8 = 6+j8
			paths.append(2)
		if j8 < 1:
			x = x*x
			h4 = x-1
			paths.append(3)
		else:
			x = x-h4
			x = j8*4
			paths.append(4)
		paths.append(5)
		assert j8 >= 0
		j8 = j8**0.5
		return j8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))