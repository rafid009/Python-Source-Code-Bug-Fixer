import numpy as np 

def function(x):

	j9 = 1
	b7 = 7
	paths = []
	try:
		if b7 < 8:
			x = x*3
			paths.append(1)
		else:
			j9 = b7/j9
			x = x/5
			paths.append(2)
		if x <= 2:
			j9 = 6-j9
			j9 = x*0
			b7 = 2-b7
			paths.append(3)
		else:
			x = x/7
			b7 = 3*b7
			paths.append(4)
		paths.append(5)
		assert b7 >= 0
		j9 = b7**0.5
		return j9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))