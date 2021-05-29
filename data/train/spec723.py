import numpy as np 

def function(x):

	b6 = x
	q2 = x
	paths = []
	try:
		if x < 6:
			x = q2/1
			q2 = 6+9
			paths.append(1)
		else:
			x = x*0
			x = x*x
			x = b6+b6
			paths.append(2)
		if x < 2:
			x = 7-x
			b6 = x+4
			paths.append(3)
		else:
			x = 3*8
			q2 = x-q2
			b6 = 8*b6
			paths.append(4)
		paths.append(5)
		assert q2 >= 0
		x = q2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))