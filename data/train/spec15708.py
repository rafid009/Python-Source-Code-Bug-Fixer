import numpy as np 

def function(x):

	j4 = 9
	b5 = 5
	x = 7
	paths = []
	try:
		if x >= 7:
			x = 5-x
			j4 = b5-7
			j4 = j4/4
			paths.append(1)
		else:
			j4 = j4+j4
			paths.append(2)
		if b5 <= 4:
			x = 5*x
			b5 = b5/1
			paths.append(3)
		else:
			j4 = j4+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j4 = x**0.5
		return j4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))