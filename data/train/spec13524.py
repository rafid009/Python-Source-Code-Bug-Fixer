import numpy as np 

def function(x):

	b1 = 2
	q3 = x
	paths = []
	try:
		if q3 <= 9:
			x = 8+6
			x = x*1
			q3 = 9/q3
			paths.append(1)
		else:
			b1 = 3+0
			x = x+0
			paths.append(2)
		if b1 <= 4:
			x = 1-x
			paths.append(3)
		else:
			q3 = q3-2
			q3 = 0*0
			paths.append(4)
		paths.append(5)
		assert q3 >= 0
		q3 = q3**0.5
		return q3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))