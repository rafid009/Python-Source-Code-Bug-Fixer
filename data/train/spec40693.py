import numpy as np 

def function(x):

	w7 = x
	j5 = 9
	paths = []
	try:
		if x < 6:
			j5 = x*5
			paths.append(1)
		else:
			w7 = j5+j5
			x = 4+x
			paths.append(2)
		if j5 < 4:
			j5 = x+w7
			x = 0+x
			w7 = w7-j5
			paths.append(3)
		else:
			x = 8/x
			x = 1*x
			paths.append(4)
		paths.append(5)
		assert j5 >= 0
		x = j5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))