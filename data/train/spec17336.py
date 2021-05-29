import numpy as np 

def function(x):

	b7 = 3
	q4 = x
	x = 4
	paths = []
	try:
		if x <= 8:
			q4 = q4+5
			q4 = q4+1
			x = 6+q4
			paths.append(1)
		else:
			x = 0+0
			b7 = b7/9
			paths.append(2)
		if b7 >= 6:
			x = x-4
			x = 5+b7
			paths.append(3)
		else:
			b7 = x*b7
			b7 = q4+x
			x = 1-2
			paths.append(4)
		paths.append(5)
		assert b7 >= 0
		b7 = b7**0.5
		return b7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))