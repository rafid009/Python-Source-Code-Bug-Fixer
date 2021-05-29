import numpy as np 

def function(x):

	q9 = x
	y5 = x
	paths = []
	try:
		if x > 6:
			x = 1/x
			paths.append(1)
		else:
			x = x+6
			q9 = q9*8
			y5 = y5*0
			paths.append(2)
		if x > 9:
			y5 = y5*1
			y5 = 5-7
			x = y5+0
			paths.append(3)
		else:
			q9 = 4-q9
			x = y5+4
			x = 8/5
			paths.append(4)
		paths.append(5)
		assert q9 >= 0
		q9 = q9**0.5
		return q9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))