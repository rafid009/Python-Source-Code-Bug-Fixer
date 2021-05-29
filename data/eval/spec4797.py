import numpy as np 

def function(x):

	q5 = x
	b9 = 0
	paths = []
	try:
		if b9 < 2:
			b9 = 9+b9
			paths.append(1)
		else:
			q5 = q5/4
			q5 = 2/q5
			paths.append(2)
		if q5 <= 6:
			x = q5*x
			b9 = b9+7
			x = x/6
			paths.append(3)
		else:
			b9 = 2/b9
			paths.append(4)
		paths.append(5)
		assert q5 >= 0
		b9 = q5**0.5
		return b9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))