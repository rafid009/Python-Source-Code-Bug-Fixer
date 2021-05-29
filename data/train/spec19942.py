import numpy as np 

def function(x):

	b1 = 8
	q2 = 4
	paths = []
	try:
		if q2 < 1:
			x = 3*0
			b1 = b1*1
			paths.append(1)
		else:
			b1 = x+b1
			x = 9-x
			paths.append(2)
		if x < 0:
			x = x*5
			q2 = q2/4
			paths.append(3)
		else:
			q2 = q2/x
			x = 0*b1
			q2 = q2+3
			paths.append(4)
		paths.append(5)
		assert b1 >= 0
		b1 = b1**0.5
		return b1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))