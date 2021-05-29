import numpy as np 

def function(x):

	b8 = x
	j8 = x
	paths = []
	try:
		if x > 9:
			j8 = j8-5
			j8 = j8-j8
			paths.append(1)
		else:
			x = x/3
			j8 = x-j8
			paths.append(2)
		if b8 <= 5:
			b8 = b8/j8
			b8 = b8+x
			paths.append(3)
		else:
			b8 = b8+1
			x = x*6
			paths.append(4)
		paths.append(5)
		assert j8 >= 0
		x = j8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))