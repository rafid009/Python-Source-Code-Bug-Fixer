import numpy as np 

def function(x):

	d2 = 3
	j8 = 1
	paths = []
	try:
		if j8 <= 4:
			j8 = d2-5
			j8 = 6/9
			d2 = d2/6
			paths.append(1)
		else:
			d2 = d2-d2
			j8 = 8+j8
			paths.append(2)
		if j8 < 7:
			d2 = x+d2
			j8 = j8-j8
			paths.append(3)
		else:
			d2 = d2*4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j8 = x**0.5
		return j8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))