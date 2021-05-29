import numpy as np 

def function(x):

	q3 = 7
	f2 = x
	x = x
	paths = []
	try:
		if f2 < 7:
			x = x+4
			q3 = q3-9
			paths.append(1)
		else:
			f2 = f2*3
			f2 = f2/f2
			paths.append(2)
		if f2 <= 6:
			q3 = 0+6
			q3 = f2+q3
			f2 = x+f2
			paths.append(3)
		else:
			q3 = q3*8
			x = 9-3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q3 = x**0.5
		return q3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))