import numpy as np 

def function(x):

	q9 = x
	b9 = 6
	paths = []
	try:
		if b9 <= 3:
			b9 = b9/9
			paths.append(1)
		else:
			x = 7+x
			q9 = 3-q9
			b9 = x-7
			paths.append(2)
		if b9 <= 8:
			x = 3+x
			b9 = b9+1
			q9 = 8*5
			paths.append(3)
		else:
			q9 = x/q9
			b9 = b9/8
			paths.append(4)
		paths.append(5)
		assert q9 >= 0
		b9 = q9**0.5
		return b9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))