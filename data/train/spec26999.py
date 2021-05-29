import numpy as np 

def function(x):

	b1 = 5
	q3 = 2
	x = x
	paths = []
	try:
		if b1 < 7:
			x = x+q3
			b1 = b1*1
			q3 = q3+x
			paths.append(1)
		else:
			b1 = 0/b1
			paths.append(2)
		if q3 <= 7:
			x = x+q3
			paths.append(3)
		else:
			x = x/3
			x = 7*x
			paths.append(4)
		paths.append(5)
		assert q3 >= 0
		x = q3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))