import numpy as np 

def function(x):

	b6 = x
	j9 = 7
	paths = []
	try:
		if b6 > 6:
			j9 = j9/1
			j9 = x*4
			paths.append(1)
		else:
			x = 7+7
			x = x/j9
			paths.append(2)
		if b6 <= 0:
			b6 = 3+b6
			paths.append(3)
		else:
			b6 = 0*b6
			b6 = x-9
			paths.append(4)
		paths.append(5)
		assert b6 >= 0
		j9 = b6**0.5
		return j9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))